import xmlrpclib
import time
import random



class Foo:
  def __init__(self):
    self.counter=0

    # Create an object to represent our server.
    server_url = 'http://127.0.0.1:20738/RPC2'
    server = xmlrpclib.Server(server_url)
    self.G = server.ubigraph
    
    self.G.clear()
    
    # Set default edge style
    self.G.set_edge_style_attribute(0, "oriented", "true")
    self.G.set_edge_style_attribute(0, "color", "#C5892F")
    
    # Default vertex style
    self.G.set_vertex_style_attribute(0, "shape", "torus")
    
    # Vertex style for leaves
    self.leaf = self.G.new_vertex_style(0)
    self.G.set_vertex_style_attribute(self.leaf, "color", "#80219C")
    self.G.set_vertex_style_attribute(self.leaf, "size", "3.0")
    print("cons")
    
    # Make a root vertex and build the tree
    self.root = self.G.new_vertex()
    x = self.subtree(self.root,8)

  # Recursive tree construction
  def subtree(self,parent,n):
    self.counter=self.counter+1
    v = self.G.new_vertex()
    e = self.G.new_edge(parent,v)
    self.G.set_edge_attribute(e, "width", str(1.0 + n))
  
    #G.set_vertex_attribute(e, "color", "#ff7f5e")
    #G.set_edge_attribute(e, "shape", "torus")
    #G.set_vertex_style_attribute(e, "shape", "sphere")
    #G.set_edge_attribute(e, "label", "ANGELICA")
  
    rand=random.randrange(0,5)
    self.G.set_edge_attribute(e, "label", "%s" % self.counter)
  
    if rand == 0:
      self.G.set_vertex_style_attribute(e, "shape", "sphere")
      self.G.set_vertex_attribute(e, "label", "foo")
    elif rand == 1:
      self.G.set_vertex_style_attribute(e, "shape", "sphere")
      self.G.set_edge_attribute(e, "shape", "sphere")
      self.G.set_vertex_attribute(e, "label", "bar")
    elif rand == 2:
      self.G.set_vertex_style_attribute(e, "shape", "sphere")
      self.G.set_vertex_attribute(e, "label", "baz")
    else:
      self.G.set_vertex_style_attribute(e, "shape", "sphere")
      self.G.set_vertex_attribute(e, "label", "zaz")
  
    if (n > 0):
      for j in range(0,2):
        v2 = self.subtree(v,n-1)
    else: 
      self.G.change_vertex_style(v, self.leaf)
      time.sleep(0.02)
    return v


if __name__ == '__main__':
  print("init")
  f=Foo() 
  print("past")
