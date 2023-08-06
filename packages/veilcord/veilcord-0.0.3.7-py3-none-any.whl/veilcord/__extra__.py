# THIS ISNT AVAILABLE PUBLICALLY YET UNLESS YOU KNOW HOW TO RUN IT WITHOUT HELP

from time       import sleep
from tls_client import Session
from requests   import post
from typing     import Literal

from .__main__ import HTTPClient


class Solver:
    def __init__(
        self, 
        session: Session = HTTPClient().session,
        service: Literal["CAPSOVLER", "ANTI[CAPTCHA]", "CAPBYPASS"] = "CAPSOLVER", # will add more in the future
        capKey: str = None,
        siteKey: str = "4c672d35-0701-42b2-88c3-78380b0db560",
        siteUrl: str = "https://discord.com",
    ):
        self.session = HTTPClient().session if session is None else session
        self.service = service
        self.capKey  = capKey
        self.siteKey = siteKey
        self.siteUrl = "https://" + siteUrl if "http" not in siteUrl else siteUrl
        
        if not capKey:
            raise ValueError("A captcha service key is required in order to solve the captcha :/")
        
    def solveCaptcha(self) -> str:
        if self.service == "CAPSOLVER":
            return self.solveGeneric(domain="https://api.capsolver.com")
        elif self.service == "ANTI[CAPTCHA]":
            return self.solveGeneric(domain="https://api.anti-captcha.com")
        elif self.service == "CAPBYPASS":
            return self.solveGeneric(domain="https://api.capbypass.com")
        elif self.service == "CUSTOM":
            return print("gay")
            # key = run(solve(
            #    siteKey, siteUrl.replace("https://", ""), session.proxies.get("http")
            # ))
            # if not key:
            #     return solver.solveCaptcha(session=session)
            # return key
        else:
            raise ValueError("invalid captcha service.")
    
    def solveGeneric(self, siteKey: str, siteUrl: str, session: Session, domain: str) -> str:
        taskType = "HCaptchaTurboTask" if "capsolver" in domain else "HCaptchaTask"
        data1 = {
            "clientKey": self.capKey,
            "task": {
                "type": taskType,
                "websiteURL": siteUrl,
                "websiteKey": siteKey,
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
                "proxy": self.getProxyFromSession(session)
            }
        }
        resp1 = post(f"{domain}/createTask", json=data1)
        
        if "ERROR_KEY_DENIED_ACCESS" in resp1.text: 
            return print("Invalid Captcha Service Key")
        
        if resp1.json().get("errorId") == 0:
            taskId = resp1.json().get("taskId")
            data = {
                "clientKey": self.capKey,
                "taskId": taskId
            }
            resp = post(f"{domain}/getTaskResult", json=data)
            status = resp.json().get("status")

            while status == "processing":
                sleep(1)
                resp = post(f"{domain}/getTaskResult", json=data)
                status = resp.json().get("status")

            if status == "ready":
                return resp.json().get("solution").get("gRecaptchaResponse")
            else:
                return self.solveCaptcha(session=session)
        else:
            return self.solveGeneric(session, domain)
    
    
    @staticmethod
    def getProxyFromSession(session: Session) -> str:
        protocol, sessionProxy = session.proxies.get("http").split("://")
        sessionProxy = sessionProxy.replace(":", "big juicy fat cock").replace("@", "big juicy fat cock")
        if len(sessionProxy.split("big juicy fat cock")) == 4:
            user, password, host, port = sessionProxy.split("big juicy fat cock")
            return f"{protocol}:{host}:{port}:{user}:{password}"
        else:
            host, port = sessionProxy.split("big juicy fat cock")
            return f"{protocol}:{host}:{port}"