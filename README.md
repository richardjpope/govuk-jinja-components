# nhsuk-jinja-components

NHS Design System components ported to jinja to use in Flask apps.

Add this line to your requirements.txt

    -e git+https://github.com/richardjpope/nhsuk-jinja-components#egg=nhsuk-jinja-components

Add the following to your Flask factory.py

    def register_templates(app):
        multi_loader = ChoiceLoader([
            app.jinja_loader,
            PrefixLoader({
                'nhsuk-jinja-components': PackageLoader('nhsukuk-jinja-components')
            })
        ])
        app.jinja_loader = multi_loader
