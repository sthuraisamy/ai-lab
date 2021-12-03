import re

# regex for removing @ and URLs
replace_vals = [(re.compile(r'@\w+'), ''), (re.compile(r'http\S+'), '')]

# convert tokens to lower case, clean tokens and trim whitespace


def pre_token_cleanup(text, replace_vals):
    '''function to pre-process the tweets'''
    text = text.lower()  # convert to lower case

    # text = replace_with(text, [('&amp;', 'and'), ('&gt;', '>'), ('&lt;', '<')])
    for replace in replace_vals:
        text = re.sub(replace[0], replace[1], text)

    text = text.strip()  # remove leading and trailing whitespace

    return text


def clean_list_values(data_df, col_name):
    '''function to clean the values in a list column'''
    # get the list of values
    list_values = data_df[col_name].tolist()

    # clean the values
    clean_list_values = []
    for value in list_values:
        clean_list_values.append(pre_token_cleanup(value, replace_vals))

    # replace the list of values with the cleaned values
    data_df[col_name] = clean_list_values

    return data_df


