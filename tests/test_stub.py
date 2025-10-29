class LoggerStub:
    def info(self, msg):
        return f"LOG: {msg}"

def test_stub_logger():
    logger = LoggerStub()
    mensaje = logger.info("ISBN validado correctamente")
    assert "LOG:" in mensaje