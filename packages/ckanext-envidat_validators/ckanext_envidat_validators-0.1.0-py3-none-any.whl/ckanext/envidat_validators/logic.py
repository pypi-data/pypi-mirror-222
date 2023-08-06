"""Validator logic for IValidators."""

import json
import logging

import ckan.lib.navl.dictization_functions as df
from ckantoolkit import _, get_validator

import ckanext.scheming.helpers as sh
from ckanext.scheming.validation import scheming_validator

log = logging.getLogger(__name__)

missing = df.missing
StopOnError = df.StopOnError
not_empty = get_validator("not_empty")


@scheming_validator
def composite_group2json(field, schema):
    """Composite field validator (legacy)."""

    def validator(key, data, errors, context):
        """Logic for composite_group2json."""
        value = ""
        for name, text in data.items():
            if name == key:
                if text:
                    value = text

        # Parse from extras into a dictionary and save it as a json dump
        if not value:
            found = {}
            prefix = key[-1] + "-"
            extras = data.get(key[:-1] + ("__extras",), {})

            extras_to_delete = []
            for name, text in extras.items():
                if not name.startswith(prefix):
                    continue
                # if not text:
                #    continue
                subfield = name.split("-", 1)[1]
                found[subfield] = text
                extras_to_delete += [name]
            if not found:
                data[key] = ""
            else:
                item_is_empty = _composite_all_empty(field, found)
                item_is_empty_and_optional = (
                    item_is_empty and not sh.scheming_field_required(field)
                )
                # Check if there is any mandatory subfield required
                for schema_subfield in field["subfields"]:
                    if (
                        schema_subfield.get("required", False)
                        and not item_is_empty_and_optional
                    ):
                        subfield_label = schema_subfield.get(
                            "label", schema_subfield.get("field_name", "")
                        )
                        subfield_value = found.get(
                            schema_subfield.get("field_name", ""), ""
                        )
                        _composite_not_empty_subfield(
                            key, subfield_label, subfield_value, errors
                        )
                if item_is_empty:
                    found = {}
                data[key] = json.dumps(found, ensure_ascii=False)

                # delete the extras to avoid duplicate fields
                for extra in extras_to_delete:
                    del extras[extra]

        # Check if the field is required
        if sh.scheming_field_required(field):
            not_empty(key, data, errors, context)

    return validator


@scheming_validator
def composite_repeating_group2json(field, schema):
    """Composite repeating field validator (legacy)."""

    def validator(key, data, errors, context):
        """Logic for composite_repeating_group2json."""
        value = ""

        for name, text in data.items():
            if name == key:
                if text:
                    value = text

        # parse from extra into a list of dictionaries and save it as a json dump
        if not value:
            found = {}
            prefix = key[-1] + "-"
            extras = data.get(key[:-1] + ("__extras",), {})

            extras_to_delete = []
            for name, text in extras.items():
                if not name.startswith(prefix):
                    continue

                # if not text:
                #    continue

                index = int(name.split("-", 2)[1])
                subfield = name.split("-", 2)[2]
                extras_to_delete += [name]

                if index not in found.keys():
                    found[index] = {}
                found[index][subfield] = text
            found_list = [element[1] for element in sorted(found.items())]

            if not found_list:
                data[key] = ""
            else:

                # check if there are required subfields missing for every item
                for index in found:
                    item = found[index]
                    item_is_empty_and_optional = _composite_all_empty(
                        field, item
                    ) and not sh.scheming_field_required(field)
                    for schema_subfield in field["subfields"]:
                        if (
                            schema_subfield.get("required", False)
                            and not item_is_empty_and_optional
                        ):
                            if type(schema_subfield.get("label", "")) is dict:
                                subfield_label = (
                                    schema_subfield.get("field_name", "")
                                    + " "
                                    + str(index)
                                )
                            else:
                                subfield_label = (
                                    schema_subfield.get(
                                        "label", schema_subfield.get("field_name", "")
                                    )
                                    + " "
                                    + str(index)
                                )

                            subfield_value = item.get(
                                schema_subfield.get("field_name", ""), ""
                            )
                            _composite_not_empty_subfield(
                                key, subfield_label, subfield_value, errors
                            )

                # remove empty elements from list
                clean_list = []
                for element in found_list:
                    if not _composite_all_empty(field, element):
                        clean_list += [element]
                # dump the list to a string
                data[key] = json.dumps(clean_list, ensure_ascii=False)

                # delete the extras to avoid duplicate fields
                for extra in extras_to_delete:
                    del extras[extra]

        # check if the field is required
        if sh.scheming_field_required(field):
            not_empty(key, data, errors, context)

    return validator


def envidat_shortname_validator(key, data, errors, context):
    """Prevent short package titles <80 char."""
    value = data.get(key)
    if not value or len(value) > 80:
        errors[key].append(_("text should be maximum 80 characters long"))
        raise StopOnError


def envidat_string_uppercase(key, data, errors, context):
    """Make string values uppercase.

    If the value is a string, make it uppercase, otherwise leave the value as it is.
    make all tags uppercase if possible.
    """
    # Plain value to uppercase
    tags = data[key]
    if isinstance(tags, str):
        data[key] = tags.upper()

    # tags to uppercase
    num = 0
    tag = data.get(("tags", num, "name"), "")
    while tag:
        data[("tags", num, "name")] = _safe_upper(tag)
        num += 1
        tag = data.get(("tags", num, "name"), "")


def envidat_minimum_tag_count(key, data, errors, context):
    """Count tags and raise an error if there are less than 5."""
    min_tags = 5
    # tags to count
    num = 0
    tag = data.get(("tags", num, "name"), "")
    while tag:
        num += 1
        tag = data.get(("tags", num, "name"), "")

    if num < min_tags:
        errors[key].append(_("at least " + str(min_tags) + " tags"))
        raise StopOnError


def envidat_minimum_description_length(key, data, errors, context):
    """Count description chars and raise an error if there are less than 100."""
    min_length = 100
    # tags to count
    description = data.get(key, "")
    description_length = len(description)

    if description_length < min_length:
        errors[key].append(
            _(
                "at least {0} characters, currently {1}".format(
                    min_length, description_length
                )
            )
        )
        raise StopOnError


@scheming_validator
def envidat_reorder(field, schema):
    """Reorder sub elements."""

    def validator(key, data, errors, context):
        """Logic for envidat_reorder."""
        try:
            field_data = json.loads(data[key])
            sorted_list = sorted(
                field_data, key=lambda k: int(k.get("order", len(field_data)))
            )
            for element in sorted_list:
                element.pop("order", 0)
            data[key] = json.dumps(sorted_list)

        except ValueError as e:
            log.error(
                "Could not reorder field {0}, exception raised {1}".format(key, e)
            )
            return

    return validator


@scheming_validator
def envidat_copy_type_general(field, schema):
    """Copy type general."""

    def validator(key, data, errors, context):
        """Logic for envidat_copy_type_general."""
        data[key] = data.get(("resource_type_general",), data[key])

    return validator


def _safe_upper(value):
    """Upper or same value if it is not a string."""
    try:
        return value.upper()
    except Exception:
        return value


def _composite_not_empty_subfield(key, subfield_label, value, errors):
    """Validate subfields are not empty.

    Function equivalent to ckan.lib.navl.validators.not_empty
    but for subfields (custom message including subfield).
    """
    if not value or value is missing:
        errors[key].append(_("Missing value at required subfield " + subfield_label))
        raise StopOnError


def _composite_all_empty(field, item):
    all_empty = True
    for schema_subfield in field["subfields"]:
        subfield_value = item.get(schema_subfield.get("field_name", ""), "")
        if subfield_value and subfield_value is not missing:
            all_empty = False
    return all_empty
