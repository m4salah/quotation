from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from auth import AuthError, requires_auth
from models import setup_db, Quote, Person, create_tables


def create_app():
    app = Flask(__name__)
    CORS(app)
    setup_db(app)
    create_tables()

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, True')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, DELETE, PATCH, OPTIONS')
        return response
    
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({
            'success': True,
            'description': 'Quotation system is running.'
        })
    
    @app.route('/quotes')
    @requires_auth('get:quotes')
    def get_quotes(jwt):
        quotes = Quote.query.order_by('id').all()
        if not quotes:
            abort(404)

        quotes_formated = [quote.format() for quote in quotes]
        return jsonify({
            'success': True,
            'quotes': quotes_formated,
            'total_quotes': len(quotes)
        })

    @app.route('/persons')
    @requires_auth('get:persons')
    def get_persons(jwt):
        persons = Person.query.order_by('id').all()
        if not persons:
            abort(404)

        persons_formated = [person.format() for person in persons]

        return jsonify({
            'success': True,
            'persons': persons_formated,
            'total_persons': len(persons)
        })

    @app.route('/quotes', methods=['POST'])
    @requires_auth('create:quote')
    def create_quote(jwt):
        body = request.get_json()
        title = body.get('title', None)
        description = body.get('description', None)
        person_id = body.get('person_id', None)

        if title is None or description is None or person_id is None:
            abort(422)
            
        try:
            
            quote = Quote(title=title, 
                          description=description, 
                          person_id=person_id)

            quote.insert()

            quotes_after_create = Quote.query.order_by('id').all()
            quotes_formated = [quote.format() for quote in quotes_after_create]

            return jsonify({
                'success': True,
                'created': quote.id,
                'quotes': quotes_formated,
                'total_quotes': len(quotes_formated)
            })
        except:
            abort(422)
    
    @app.route('/persons', methods=['POST'])
    @requires_auth('create:person')
    def create_person(jwt):
        body = request.get_json()
        name = body.get('name', None)
        if name is None:
            abort(422)
            
        try:
            person = Person(name=name)
            person.insert()
            print("here")
            print(person.name)
            persons_after_create = Person.query.order_by('id').all()
            persons_formated = [person.format() for person in persons_after_create]
            return jsonify({
                'success': True,
                'created': person.id,
                'persons': persons_formated,
                'total_persons': len(persons_after_create)
            })
        except:
            abort(422)

    @app.route('/quotes/<int:id>', methods=['PATCH'])
    @requires_auth('edit:quote')
    def edit_quote(jwt, id):
        body = request.get_json()
        print(body)
        
        title = body.get('title', None)
        description = body.get('description', None)
        person_id = body.get('person_id', None)
        
        quote = Quote.query.get_or_404(id) 
        try:
            if title:
                quote.title = title
            if description:
                quote.description = description
            if person_id:
                quote.person_id = person_id 
            
            quote.update()

            return jsonify({
                'success': True,
                'quote_id': quote.id,
            })
        except:
            abort(422)
    
    
    @app.route('/persons/<int:id>', methods=['PATCH'])
    @requires_auth('edit:person')
    def edit_person(jwt, id):
        body = request.get_json()
        print(body)
        name = body.get('name', None)
        
        person = Person.query.get_or_404(id)
        try:
            if name:
                person.name = name

            return jsonify({
                'success': True,
                'person_id': person.id,
            })
        except:
            abort(422)
    
    @app.route('/quotes/<int:id>', methods=['DELETE'])
    @requires_auth('remove:quote')
    def remove_quote(jwt, id):
        quote = Quote.query.get_or_404(id)
        try:
            quote.delete()
            return jsonify({
                'success': True,
                'id': id
            })
        except:
            abort(422)
    
    
    @app.route('/persons/<int:id>', methods=['DELETE'])
    @requires_auth('remove:person')
    def remove_person(jwt, id):
        person = Person.query.get_or_404(id)
        try:
            person.delete()
            return jsonify({
                'success': True,
                'id': id
            })
        except:
            abort(422)
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        return jsonify({
            "success": False,
            "error": ex.status_code,
            'message': ex.error
        }), 401
    return app


app = create_app()
if __name__ == '__main__':
    app.run()