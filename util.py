def filter_json(json, letter):
    result = []
    for index, data in enumerate(json["usernames"]):
        if data[0].lower() == letter:
            dictionary = {
                "username": data,
                "githubLink": json["githubLinks"][index],
                "filename": json["filenames"][index],
                "content": json["contents"][index],
            }
            result.append(dictionary)
    return result
