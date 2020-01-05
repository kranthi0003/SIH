import os
import urllib.request
from flask import Flask, flash, request, redirect, render_template, session, url_for
from werkzeug.utils import secure_filename
from forms import UploadForm, EntryForm, SearchForm, QuesSearchForm
import PyPDF2
from myclass import es
import elasticsearch

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.secret_key = "SIH"

UPLOAD_FOLDER ='G:/SIH/Project/SIH/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convertor(filename):
	pdfFileObj = open('G:/SIH/Project/SIH/uploads/'+filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	print("Number of pages:-"+str(pdfReader.numPages))
	num = pdfReader.numPages
	i =0
	file_res = open('G:/SIH/Project/SIH/converts/'+filename.split('.')[0]+'.txt','w',encoding='UTF-8')
	while(i<num):
		pageObj = pdfReader.getPage(i)
		text=pageObj.extractText()
		#print(text)
		file_res.write('\n\nPage: '+str(i+1)+'\n\n'+text)
		i=i+1

@app.route('/', methods = ['GET', 'POST'])
@app.route('/start', methods = ['GET', 'POST'])
def upload_form():
	form1 = UploadForm()
	form2 = QuesSearchForm()
	res = []
	es = elasticsearch.Elasticsearch()
	if(form1.validate_on_submit() and ('submit' in request.form)):
		if(request.form['submit'] == 'Submit'):
			print('Hi1')
			if 'file' not in request.files:
				flash('No file part')
				return redirect(request.url)
			file = request.files['file']
			print(file.filename)
			if file.filename == '':
				flash('No file selected for uploading')
				return redirect(request.url)
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				flash('File successfully uploaded')
				convertor(filename)
				print(filename.split('.')[0])
				#session['filename'] = filename.split('.')[0]
				filename = filename.split('.')[0]
				author = 'myind4'
				book = open('G:/SIH/Project/SIH/converts/'+filename+'.txt')
				lineNum = 0
				txtNum = 0
				try:
					for lineText in book:
					    lineNum += 1
					    if len(lineText) > 0:
					        txtNum += 1
					        es.index(index=author, id=txtNum, body = {'lineNum': lineNum,'text': lineText})
				except UnicodeDecodeError as e:
					print("Decode error at: " + str(lineNum) + ':' + str(txtNum))
					print(e)
					book.close()
				print(es.get(index=author, id=txtNum))

			else:
				flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
				return redirect(request.url)

	if(form2.validate_on_submit() and ('submit' in request.form)):
		if(request.form['submit'] == 'Search'):
			print('HI')
			'''print('HI')
			session['index'] = form2.index.data
			session['query'] = form2.search.data
			print(form2.index.data)
			print(form2.search.data)
			return redirect(url_for('search'))'''

			author = form2.index.data
			query = form2.search.data
			print(form2.index.data)
			print(form2.search.data)
			numResults = 10

			results = es.search(
				index=author,
				body={
				    "size": numResults,
				    "query": {"match": {"text": {"query": query}}}})
			print('befRes')
			print(results)

			hitCount = results['hits']['total']['value']
			print(hitCount)
			if hitCount > 0:
				if hitCount is 1:
				    print(str(hitCount) + ' result')
				else:
				    print(str(hitCount) + ' results')
				    
				for hit in results['hits']['hits']:
				    text = hit['_source']['text']
				    lineNum = hit['_source']['lineNum']
				    score = hit['_score']
				    title = hit['_type']
				    if lineNum > 1:
				        previousLine = es.get(index=author,id=lineNum-1)
				    #nextLine = es.get(index=author, id=lineNum+1)
				    res.append(title + ': ' + str(lineNum) + ' (' + str(score) + '): ')
				    res.append(previousLine['_source']['text'] + text + nextLine['_source']['text'])
				print(res)
			else:
				print('No results')

			#return render_template('start.html', res=res)
	res = res	
	return render_template('start.html', form1 = form1, form2 = form2, res = res)


'''@app.route('/search', methods = ['GET', 'POST'])
def search():
	numResults = 10
	es = elasticsearch.Elasticsearch()

	results = es.search(
		index=author,
		body={
		    "size": numResults,
		    "query": {"match": {"text": {"query": query}}}})

	print(results)

	hitCount = results['hits']['total']['value']
	print(hitCount)
	if hitCount > 0:
		if hitCount is 1:
		    print(str(hitCount) + ' result')
		else:
		    print(str(hitCount) + ' results')
		    
		for hit in results['hits']['hits']:
		    text = hit['_source']['text']
		    lineNum = hit['_source']['lineNum']
		    score = hit['_score']
		    title = hit['_type']
		    if lineNum > 1:
		        previousLine = es.get(index=author,id=lineNum-1)
		    nextLine = es.get(index=author, id=lineNum+1)
		    res.append(title + ': ' + str(lineNum) + ' (' + str(score) + '): ')
		    res.append(previousLine['_source']['text'] + text + nextLine['_source']['text'])
	else:
		print('No results')

	#print(form)

	return render_template('search.html', res=res)'''

if __name__ == "__main__":
    app.run(debug=True)

