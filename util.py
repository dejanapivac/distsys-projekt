def filter_json(json, letter):
    result = []
    for index, data in enumerate(json["usernames"]):
        if data.lower().startsWith(letter):
            dictionary = {
                "username": data,
                "githublinkovi": json["githubLinks"][index],
                "filename": json["filename"][index],
                "content": json["content"][index],
            }
            result.append(dictionary)
    return result
