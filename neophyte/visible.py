class visible:
   
    def display(self, host):
        for string in self.strings:
            host.curse.addstr(string)
            host.curse.refresh()

        host.visibles.update({self.name: self.strings})
        
    def hide(self, host):
        host.visibles.pop(self.name)
        host.curse.clear()
        for vs in host.visibles.values():
            for string in vs:
                host.curse.addstr(string)
                host.curse.refresh()

