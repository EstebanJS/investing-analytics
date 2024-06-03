from flask import request, jsonify
from api.controllers import Controller
import concurrent.futures

def setup_routes(app):
    controller = Controller()

    @app.route('/api/get-company-info', methods=['POST'])
    def scrape_financials_scraper():
        CompanyName = request.json.get('CompanyName')
        
        if not CompanyName:
            return jsonify({'error': 'Missing URL parameter'}), 400
        
        try:
            result = controller.get_company_info(CompanyName)
            return jsonify(result.to_dict(orient="records"))
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        