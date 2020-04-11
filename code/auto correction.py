
import nltk
from nltk.tokenize import word_tokenize,wordpunct_tokenize
text=str (input('please tell me about your symptoms : '))
token=word_tokenize(text)
print(token)
token1= wordpunct_tokenize(text)
# print(token1)
tagged=nltk.pos_tag(token)
print (tagged)
class NLP:
    def __init__(self):
        self.info = []
    def extractor(self):
        chunkgram=r"""chunk : {<.*>+}
                        		}<VB.?|IN|DT|TO|NNS|CC>+{
                 chunk:
                    {<DT><NN>+<VBG>|<DT><NN|NNS>+}
                    }<DT>{
                    chunk:
                    {<NN><IN><DT>}
                    }<NN>{
                    }<DT>{
                    chunk:
                    {<VB|VBN><RP|IN>}
                    }<VB>{
                    }<VBN>{
                    chunk:
                    {<CD>}
                          chunk:
                    {<WP><VBZ><DT><NN><NN><IN><NNP|NN>+}
                    }<WP>{
                    }<VBZ>{
                    }<DT>{
                    }<IN>{
                    <NN>}{<NN>
                          chunk:
                    {<JJ>?<NN>+}
                    <JJ>}{<NN>
                    <NN>}{<NN>
                                """
        self.info=[]
        chunkparser=nltk.RegexpParser(chunkgram)
        chunked=chunkparser.parse(tagged)
        chunked.draw() 
        for element in chunked:
            if hasattr(element, 'label'):
                temp = ' '.join(e[0] for e in element)
                self.info.append(temp)
        return self.info
a=  NLP()      
print(a.extractor())