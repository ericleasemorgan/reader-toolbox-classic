from helper import helper

# HTTP RESPONSE CODES
RC_200 = 200  # success
RC_301 = 301  # redirect
RC_404 = 404  # file not found


# HTTP HEADERS
CONTENT_HEADER = 'content-type'
HTML_CONTENT = 'text/html'


def not_found() -> str:
    return """
    <div class="row">
        <div class="col-md-12">
            <div class="error-template">
                <h1>
                    Oops!</h1>
                <h2>
                    404 Not Found</h2>
                <div class="error-details">
                    Requested page not found!
                </div>
            </div>
        </div>
    </div>"""


def query_form(**kwargs) -> str:
    query_form = ""
    database_selects = ""
    for idx, dbname in enumerate(helper.find_dbs()):
        checked = "checked" if idx == 0 else ""
        database_selects += f"""
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="database" id="{dbname}" value="{dbname}" {checked}>
                <label class="form-check-label" for="{dbname}">{dbname}</label>
            </div>
        """
    if kwargs.get('content') and kwargs.get('content') == "query_err":
        query_form = f"""<div class='alert alert-danger' role='alert'>
        Error running query - <span class="font-weight-bold">{kwargs.get('results')}</span>!</div>"""
    query_form += f"""
    <form method="POST" enctype="multipart/form-data" action="/query/run">
    <fieldset class="form-group row">
        <div class="col-8">
            <legend>Select Database</legend>
            {database_selects}
        </div>
    </fieldset>
    <div class="form-group row">
        <div class="col-8">
            <div class="input-group">
                <div class="input-group-prepend">
                <div class="input-group-text">SQLite Query</div>
                </div>
                <input id="query" name="query" placeholder="sqlite query to execute" type="text" required="required" class="form-control">
            </div>
        </div>
    </div>
    <div class="form-group row">
        <div class="col-8">
        <button name="submit" type="submit" class="btn btn-primary">Submit</button>
        </div>
    </div>
    </form>
    """
    return query_form


def rows(content) -> str:
    table = """<div class='alert alert-success' role='alert'>
        Query results found below!  
        Click <a class='alert-link' href="/index">here</a> to run another.</div>"""
    table += "<table class='table table-striped'>"
    headers = []
    for row in content:
        if not headers:
            table += "<thead><tr>"
            for key in dict(row).keys():
                table += f"<th scope='col'>{key}</th>"
                headers.append(key)
            table += "</tr></thead>"
            table += "<tbody>"
        r = dict(row)
        table += "<tr>"
        for idx, header in enumerate(headers):
            if idx == 0:
                table += f"<th scope='row'>{r[header]}</th>"
            else:
                table += f"<td>{r[header]}</td>"
        table += "</tr>"
    table += "</tbody></table>"
    return table


def cookbook() -> str:
    return """
    <table class="table table-striped">
    <caption style="caption-side: top;">List of common queries</caption>
    <thead>
        <tr>
        <th scope="col">Description</th>
        <th scope="col">Query</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">Number of items in the collection; 'How big is my corpus?'</th>
            <td>select count(id) from bib;</td>
        </tr>
        <tr>
            <th scope="row">Average length of all items measured in words; "More or less, how big is each item?"</th>
            <td>select rtrim(round(avg(words)), '.0') from bib;</td>
        </tr>
        <tr>
            <th scope="row">Average readability score of all items (0 = difficult; 100 = easy)</th>
            <td>select rtrim(round(avg(flesch)), '.0') from bib;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 statistically significant keywords; "What is my collection about?"</th>
            <td>select count(keyword) as c, keyword from wrd group by keyword order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 lemmatized nouns; "What is discussed?"</th>
            <td>select count(lemma) as c, lemma from pos where pos is 'NN' or pos is 'NNS' group by lemma order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 proper nouns; "What are the names of persons or places?"</th>
            <td>select count(token) as c, token from pos where pos LIKE 'NNP%' group by token order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 personal pronouns nouns; "To whom are things referred?"</th>
            <td>select count(lower(token)) as c, lower(token) from pos where pos is 'PRP' group by lower(token) order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 lemmatized verbs; "What do things do?"</th>
            <td>select count(lemma) as c, lemma from pos where pos like 'V%' group by lemma order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 lemmatized adjectives and adverbs; "How are things described?"</th>
            <td>select count(lemma) as c, lemma from pos where (pos like 'J%' or pos like 'R%') group by lemma order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 lemmatized superlative adjectives; "How are things described to the extreme?"</th>
            <td>select count(lemma) as c, lemma from pos where (pos is 'JJS') group by lemma order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 lemmatized superlative adverbs; "How do things do to the extreme?"</th>
            <td>select count(lemma) as c, lemma from pos where (pos is 'RBS') group by lemma order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 names of people; "Who is mentioned in the corpus?"</th>
            <td>select count(entity) as c, entity from ent where type is 'PERSON' group by entity order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 names of organizations; "What group of people are in the corpus?"</th>
            <td>select count(entity) as c, entity from ent where (type is 'ORG') group by entity order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 names of places; "What locations are mentioned in the corpus?"</th>
            <td>select count(entity) as c, entity from ent where (type is 'GPE' or type is 'LOC') group by entity order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 Internet domains; "What Webbed places are alluded to in this corpus?"</th>
            <td>select count(lower(domain)) as c, lower(domain) from url group by domain order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 URLs; "What is hyperlinked from this corpus?"</th>
            <td>select count(url) as c, url from url group by url order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 email addresses; "Who are you gonna call?"</th>
            <td>select count(lower(address)) as c, lower(address) from adr group by address order by c desc limit 50;</td>
        </tr>
        <tr>
            <th scope="row">Top 50 positive assertions; "What sentences are in the shape of noun-verb-noun?"</th>
            <td>SELECT COUNT( LOWER( t.token || ' ' || c.token || ' ' || d.token ) ) AS frequency, ( LOWER( t.token || ' ' || c.token || ' ' || d.token ) ) AS sentence FRO</td>
        </tr>
        <tr>
            <th scope="row">Sizes of items; "Measures in words, how big is each item?"</th>
            <td>select words, id from bib order by words desc;</td>
        </tr>
        <tr>
            <th scope="row">Readability of items; "How difficult is each item to read?"</th>
            <td>select rtrim(round(flesch)) as f, id from bib order by f desc;</td>
        </tr>
        <tr>
            <th scope="row">Item summaries; "In a narrative form, how can each item be abstracted?"</th>
            <td>select id, summary || '' from bib order by id;</td>
        </tr>
    </tbody>
    </table>"""


def display(path: str, **kwargs):
    if path == "index":
        body = query_form(**kwargs) + cookbook()
        return template(body)
    elif path == "rows":
        return template(rows(kwargs.get('results')))
    elif path == "not_found":
        return template(not_found)


def template(html_body: str):
    return """
    <!doctype html>
    <html lang="en">
    <head>
    <title>Distant Reader Toolbox</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    </head>
    <body><div class="container p-1">""" + html_body + """</div></body></html>"""
