import explorerhat, signal, time
import cherrypy
import string  

#pip install cherrypy
cherrypy.config.update("server.conf")

class RobotServer(object):
    def __init__(self, initialcommand):
        self.status = "stop"
        
        explorerhat.analog.one.changed(self.handle_analog)
        
        self.initialcommand = initialcommand
        # TODO : make it start initial command

    @cherrypy.expose
    def foward(self, speed=90):
        explorerhat.motor.one.forward(speed)
        explorerhat.motor.two.forward(speed)
        self.status = "forward"
        return self.status
    
    @cherrypy.expose
    def index(self):
        return self.status
    
        
    #Replicate original k9 interface
    @cherrypy.expose
    def k9(self, motor="stop"):
        # TODO : call the appropriate function
        return self.status
    
  
    def handle_analog(pin, value):
        print (pin.name, value)
        if (pin.name == "one" and value > 2):
            self.oldstatus = self.status
            self.status = "danger"
            explorerhat.motor.one.stop()
            explorerhat.motor.two.stop()
            time.sleep(0.4)
            explorerhat.motor.one.backward()
            explorerhat.motor.two.backward()
            time.sleep(1.5)
            explorerhat.motor.one.forward()
            explorerhat.motor.two.backward()
            time.sleep(1)
            
            self.forward()
            # TODO : restart old command
            #self.status = self.oldstatus

if __name__ == '__main__':
    cherrypy.quickstart(RobotServer("foward", config="app.conf")
    
    
    
