import uuid
import time
import datetime
from IPython.display import HTML, Javascript, display

class ProgressBar:
    def __init__(self):
        self.id = str(uuid.uuid4())
        display(HTML('<progress id="%s" value="0" max="100" style="width: 300px"></progress> <span id="%s"></span>' %
            (self.id + 'progbar', self.id + 'text')
        ))
        self.start = None
    def update(self, progress, outof=1.0, modrate=None):
        if isinstance(progress, str):            
            display(Javascript('''
            var bar = document.getElementById('%s');
            var text = document.getElementById('%s');
            bar.removeAttribute('value');
            text.innerText = '%s';
            ''' % (self.id + 'progbar', self.id + 'text', progress)))
            return
        
        if modrate is not None and progress % modrate != 0:
            return
        
        if self.start is None:
            self.start = time.time()
        
        portion = float(progress) / outof
        elapsed = (time.time() - self.start)
        
        if portion != 0:
            ETC = datetime.timedelta(seconds=round((elapsed / portion)-elapsed))
        else:
            ETC = 'unknown'
        
        text = '%.1f%%, %s elapsed, %s ETC' % (
            portion*100.0,
            datetime.timedelta(seconds=round(elapsed)),
            ETC
            )
        
        self.last_update = time.time()
        
        display(Javascript('''
        var bar = document.getElementById('%s');
        var text = document.getElementById('%s');
        bar.value = %s;
        bar.max = %s;
        text.innerText = '%s';
        ''' % (self.id + 'progbar', self.id + 'text', progress, outof, text)))
    def done(self):
        self.update(1, 1)