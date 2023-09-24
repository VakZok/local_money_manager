from datetime import datetime

def convert_date(original_date):
    # Define the input and output date formats
    input_format = "%d.%m.%Y"
    output_format = "%Y-%m-%d"

    # Parse the original date using the input format
    parsed_date = datetime.strptime(original_date, input_format)
    # Format the parsed date to the output format
    mysql_date = parsed_date.strftime(output_format)

    return mysql_date