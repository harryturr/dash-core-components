"""
Autogenerated file
DO NOT EDIT.
"""
import typing

from dash_component_system import (
    DashComponent, UNDEFINED, Undefined, ComponentProp
)


class Textarea(DashComponent):
    """
    A basic HTML textarea for entering multiline text.
    """
    _namespace = 'dash_core_components'
    _typename = 'Textarea'
    available_wildcard_properties = [

    ]
    id = ComponentProp('id', UNDEFINED, False)
    value = ComponentProp('value', UNDEFINED, False)
    autoFocus = ComponentProp('autoFocus', UNDEFINED, False)
    cols = ComponentProp('cols', UNDEFINED, False)
    disabled = ComponentProp('disabled', UNDEFINED, False)
    form = ComponentProp('form', UNDEFINED, False)
    maxLength = ComponentProp('maxLength', UNDEFINED, False)
    minLength = ComponentProp('minLength', UNDEFINED, False)
    name = ComponentProp('name', UNDEFINED, False)
    placeholder = ComponentProp('placeholder', UNDEFINED, False)
    readOnly = ComponentProp('readOnly', UNDEFINED, False)
    required = ComponentProp('required', UNDEFINED, False)
    rows = ComponentProp('rows', UNDEFINED, False)
    wrap = ComponentProp('wrap', UNDEFINED, False)
    accessKey = ComponentProp('accessKey', UNDEFINED, False)
    className = ComponentProp('className', UNDEFINED, False)
    contentEditable = ComponentProp('contentEditable', UNDEFINED, False)
    contextMenu = ComponentProp('contextMenu', UNDEFINED, False)
    dir = ComponentProp('dir', UNDEFINED, False)
    draggable = ComponentProp('draggable', UNDEFINED, False)
    hidden = ComponentProp('hidden', UNDEFINED, False)
    lang = ComponentProp('lang', UNDEFINED, False)
    spellCheck = ComponentProp('spellCheck', UNDEFINED, False)
    style = ComponentProp('style', UNDEFINED, False)
    tabIndex = ComponentProp('tabIndex', UNDEFINED, False)
    title = ComponentProp('title', UNDEFINED, False)
    n_blur = ComponentProp('n_blur', 0, False)
    n_blur_timestamp = ComponentProp('n_blur_timestamp', -1, False)
    n_clicks = ComponentProp('n_clicks', 0, False)
    n_clicks_timestamp = ComponentProp('n_clicks_timestamp', -1, False)
    loading_state = ComponentProp('loading_state', UNDEFINED, False)

    def __init__(
        self,
        id=UNDEFINED,
        value=UNDEFINED,
        autoFocus=UNDEFINED,
        cols=UNDEFINED,
        disabled=UNDEFINED,
        form=UNDEFINED,
        maxLength=UNDEFINED,
        minLength=UNDEFINED,
        name=UNDEFINED,
        placeholder=UNDEFINED,
        readOnly=UNDEFINED,
        required=UNDEFINED,
        rows=UNDEFINED,
        wrap=UNDEFINED,
        accessKey=UNDEFINED,
        className=UNDEFINED,
        contentEditable=UNDEFINED,
        contextMenu=UNDEFINED,
        dir=UNDEFINED,
        draggable=UNDEFINED,
        hidden=UNDEFINED,
        lang=UNDEFINED,
        spellCheck=UNDEFINED,
        style=UNDEFINED,
        tabIndex=UNDEFINED,
        title=UNDEFINED,
        n_blur=0,
        n_blur_timestamp=-1,
        n_clicks=0,
        n_clicks_timestamp=-1,
        loading_state=UNDEFINED,
    ):
        # type: (typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Dict[str, typing.Union[bool, str]], Undefined]) -> None # noqa: E501
        """
        :param id: The ID of this component, used to identify dash
            components in callbacks. The ID needs to be unique
            across all of the components in an app.
        :param value: The value of the textarea
        :param autoFocus: The element should be automatically focused after
            the page loaded.
        :param cols: Defines the number of columns in a textarea.
        :param disabled: Indicates whether the user can interact with the
            element.
        :param form: Indicates the form that is the owner of the element.
        :param maxLength: Defines the maximum number of characters allowed
            in the element.
        :param minLength: Defines the minimum number of characters allowed
            in the element.
        :param name: Name of the element. For example used by the server to
            identify the fields in form submits.
        :param placeholder: Provides a hint to the user of what can be
            entered in the field.
        :param readOnly: Indicates whether the element can be edited.
        :param required: Indicates whether this element is required to fill
            out or not.
        :param rows: Defines the number of rows in a text area.
        :param wrap: Indicates whether the text should be wrapped.
        :param accessKey: Defines a keyboard shortcut to activate or add
            focus to the element.
        :param className: Often used with CSS to style elements with common
            properties.
        :param contentEditable: Indicates whether the element's content is
            editable.
        :param contextMenu: Defines the ID of a <menu> element which will
            serve as the element's context menu.
        :param dir: Defines the text direction. Allowed values are ltr
            (Left-To-Right) or rtl (Right-To-Left)
        :param draggable: Defines whether the element can be dragged.
        :param hidden: Prevents rendering of given element, while keeping
            child elements, e.g. script elements, active.
        :param lang: Defines the language used in the element.
        :param spellCheck: Indicates whether spell checking is allowed for
            the element.
        :param style: Defines CSS styles which will override styles
            previously set.
        :param tabIndex: Overrides the browser's default tab order and
            follows the one specified instead.
        :param title: Text to be displayed in a tooltip when hovering over
            the element.
        :param n_blur: Number of times the textarea lost focus.
        :param n_blur_timestamp: Last time the textarea lost focus.
        :param n_clicks: Number of times the textarea has been clicked.
        :param n_clicks_timestamp: Last time the textarea was clicked.
        :param loading_state: Object that holds the loading state object
            coming from dash-renderer
        """
        DashComponent.__init__(self, locals())
