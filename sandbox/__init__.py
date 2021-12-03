from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.Config')

    from . import db
    db.init_app(app)

    from . import product
    app.register_blueprint(product.bp)
    app.add_url_rule('/', endpoint='index')

    return app


if __name__ == "__main__":
    create_app().run()
