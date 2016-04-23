from twisted.internet.defer import Deferred


def callback1(result):
    print("Callback1 said:", result)
    return result


def callback2(result):
    print("Callback2 said:", result)


def callback3(result):
    raise (Exception("callback3"))


def errback1(failure):
    print("Errback1 had an error on", failure)
    return failure


def errback2(failure):
    raise Exception("errback2")


def errback3(failure):
    print("Errback3 took care of", failure)
    return "Everything is fine now."


print("3.4.1. -----------------")
d = Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.callback("Test")

print("3.4.2. -----------------")
d = Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.addCallback(callback3)
d.callback("Test")

print("3.4.3. -----------------")
d = Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.addCallback(callback3)
d.addErrback(errback3)
d.callback("Test")

print("3.4.4. -----------------")
d = Deferred()
d.addErrback(errback1)
d.errback(Exception("Test"))

print("3.4.5. -----------------")
d = Deferred()
d.addErrback(errback1)
d.addErrback(errback3)
d.errback(Exception("Test"))

print("3.4.6. -----------------")
d = Deferred()
d.addErrback(errback2)
d.errback(Exception("Test"))

print("3.5.1. -----------------")
d = Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.addCallback(callback3, errback3)
d.callback("Test")

print("3.5.2. -----------------")
d = Deferred()
d.addCallback(callback3)
d.addCallbacks(callback2, callback3)
d.addCallbacks(callback1, callback2)
d.callback("Test")
