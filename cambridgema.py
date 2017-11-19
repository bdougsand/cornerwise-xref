import cloud


@cloud.aws_lambda
def getref(req):
    section = req["ordinance_section"]
    if not section:
        return (500, {"error": "ordinance_section parameter missing"})

    article = section.split(".")[0]

    try:
        if 1 <= int(article) <= 22:
            return cloud.redirect(
                f"http://www.cambridgema.gov/CDD/externallinks/zoningordinance/article{article}"
            )
        else:
            return (404, {"error": f"No article {article} exists."})
    except ValueError:
        return (500, {"error": "Article must be an integer"})
