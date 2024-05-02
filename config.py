import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    GOBGP_URI = os.environ.get("GOBGP_URI", "localhost:50051")
    WANGUARD_BASE_URI = os.environ.get("WANGUARD_BASE_URI", "http://localhost/wanguard-api")
    WANGUARD_USERNAME = os.environ.get("WANGUARD_USERNAME", "admin")
    WANGUARD_PASSWORD = os.environ.get("WANGUARD_PASSWORD", "admin")
    WANGUARD_IP_ZONE = os.environ.get("WANGUARD_IP_ZONE", "IP Zone")
    EXABGP_CMD = os.environ.get("EXABGP_CMD", "/run/exabgp/exabgp.in")
    EXABGP_ASN = os.environ.get("EXABGP_ASN", "65002")
    EXABGP_COMMUNITY = os.environ.get("EXABGP_COMMUNITY", "")
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
