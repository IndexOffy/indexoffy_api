import os
from indexoffy.app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("DEBUG", True)
    host = os.environ.get("HOST", "localhost")
    
    app.run(host=host, port=port, debug=debug)