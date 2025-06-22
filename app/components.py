import streamlit as st

def numeric_input(label, min_val, max_val, default, step=None, help_text=None):
    """
    Streamlit number input wrapper that ensures consistent step type.

    Args:
        label (str): Label for the input.
        min_val (int or float): Minimum allowed value.
        max_val (int or float): Maximum allowed value.
        default (int or float): Default value.
        step (int or float or None): Step size (optional).
        help_text (str or None): Help tooltip text.

    Returns:
        int or float: The input value.
    """
    if step is None:
        # Match step type to default type to avoid Streamlit error
        if isinstance(default, int):
            step = 1
        else:
            step = 0.1

    return st.number_input(label, min_value=min_val, max_value=max_val, value=default, step=step, help=help_text)


def selectbox(label, options, help_text=None):
    return st.selectbox(label, options=options, help=help_text)


def checkbox(label, help_text=None):
    return st.checkbox(label, help=help_text)
