"""This module contains format variable for all the annotations."""

from collections import namedtuple

__all__ = [
    "Layer",
    "Page",
    "Span",
    "Text",
    "Correction",
    "ErrorCandidate",
    "CrossVolSpan",
    "SubText",
    "Peydurma",
    "Tsawa",
    "Quotation",
    "Sabche",
    "Yigchung",
    "PechaTitle",
    "PotiTitle",
    "ChapterTitle",
    "Author",
    "AnnType",
]


class AnnType:
    # Layout tags
    pecha_title = "Pecha Title"
    poti_title = "Poti Title"
    chapter_title = "Chapter Title"
    author = "Author"
    yigchung = "Yigchung"
    pagination = "Pagination"
    correction = "Correction"
    error_candidate = "Error Candidate"
    peydurma = "Peydurma"
    tsawa = "Tsawa"
    quotation = "Qoutation"

    objects = {
        pecha_title: PechaTitle,
        poti_title: PotiTitle,
        chapter_title: ChapterTitle,
        author: Author,
        yigchung: Yigchung,
        pagination: Page,
        correction: Correction,
        error_candidate: ErrorCandidate,
        peydurma: Peydurma,
        tsawa: Tsawa,
        quotation: Quotation,
    }


class _attr_names:
    # Layer
    ID = "id"  # Uique id for annotation of specific Pecha or Abstract work. type: str
    ANNOTATION_TYPE = "annotation_type"  # Name of annotation, type: str
    REVISION = "revision"  # Revision number. type: int
    ANNOTATION = "annotations"  # Annotations are stored in list . type: dict

    # Spans
    SPAN = "span"
    START = "start"
    END = "end"

    # Page
    PAGE_INDEX = "page_index"  # Page number based on Volume specified, type: int
    PAGE_INFO = "page_info"  # Page information. type: str
    PAGE_REFERENCE = "reference"  # Any reference of page, eg: img_url. type: str

    # Correction
    CORRECTION = "correction"  # Correct text suggestion. type: str
    CERTAINTY = "certainty"  # Certainty of the suggested correct text. type: int

    # Peydurma
    NOTE = "note"  # syls, word or phrase to be compared to other publication


def Layer(id_, type_, rev=f"{1:05}"):
    return {
        _attr_names.ID: id_,
        _attr_names.ANNOTATION_TYPE: type_,
        _attr_names.REVISION: rev,
        _attr_names.ANNOTATION: {},
    }


def Span(start, end):
    return {_attr_names.START: start, _attr_names.END: end}


##### INDEX Layer #####
# Cross vol Span
CrossVolSpan = {"vol": None, "span": None}

# Sub_text annotation
SubText = {"work": None, "span": []}  # index of the sub_text  # span of the sub_text

# Text annotation
Text = {
    "work": None,  # id of the `text`. type: int
    "parts": [],  # list of SubText
    "span": [],  # list of CrossVolSpan
}

#### ANNOTATIONS Layers #####
def Page(span, page_index=None, page_info=None, page_ref=None):
    return {
        _attr_names.PAGE_INDEX: page_index,
        _attr_names.PAGE_INFO: page_info,
        _attr_names.PAGE_REFERENCE: page_ref,
        _attr_names.SPAN: span,
    }


def Correction(span, correction=None, certainty=None):
    return {
        _attr_names.CORRECTION: correction,
        _attr_names.CERTAINTY: certainty,
        _attr_names.SPAN: span,
    }


def ErrorCandidate(span):
    return {_attr_names.SPAN: span}


def Peydurma(span, note=None):
    return {_attr_names.NOTE: note, _attr_names.SPAN: span}


def PechaTitle(span):
    return {_attr_names.SPAN: span}


def PotiTitle(span):
    return {_attr_names.SPAN: span}


def Author(span):
    return {_attr_names.SPAN: span}


def ChapterTitle(span):
    return {_attr_names.SPAN: span}


def Tsawa(span):
    return {_attr_names.SPAN: span}


def Quotation(span):
    return {_attr_names.SPAN: span}


def Sabche(span):
    return {_attr_names.SPAN: span}


def Yigchung(span):
    return {_attr_names.SPAN: span}
