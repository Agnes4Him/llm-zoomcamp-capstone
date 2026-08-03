def calculate_cost(input_tokens: int, output_tokens: int) -> float:
    INPUT_PRICE = 0.40   # USD per 1M input tokens
    OUTPUT_PRICE = 1.60  # USD per 1M output tokens
    """
    Calculate LLM API cost.

    Args:
        input_tokens: Number of input tokens.
        output_tokens: Number of output tokens.

    Returns:
        Total cost in USD.
    """

    input_cost = (input_tokens / 1_000_000) * INPUT_PRICE
    output_cost = (output_tokens / 1_000_000) * OUTPUT_PRICE

    return round(input_cost + output_cost, 8)