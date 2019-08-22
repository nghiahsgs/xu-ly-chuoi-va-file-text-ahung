import io
import re
def writeFileLine(filename, nd_line):
	f = open(filename, "a")
	f.write(nd_line + '\n')
	f.close()
def writeUtf8(filename,nd_line):
    f = io.open(filename, mode="a", encoding="utf-8")
    # f.writelines("")
    f.write(nd_line + '\n')
    f.close()

nd_line="vendor_guid,object_type,title,description,display_name,calculation_method,calculation_int,workflow_state,parent_guids,mastery_points,ratings"
writeUtf8('kq.txt',nd_line)

chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
f = io.open("Learning Outcomes.txt", mode="r", encoding="utf-8")
list_lines=f.readlines()
#print(len(list_lines))
#read file line by line
current_group=''
for line in list_lines:
    if line=="":
        continue
    #print(line)
    #check danh muc pattern: number.number
    kq1=re.search(r'(((\d)+\.)+\d )',line)
    #check danh muc pattern:number
    kq2=re.search(r'( \d )',line)
    
    
    
    #1.1  KIẾN THỨC TOÁN HỌC VÀ KHOA HỌC CƠ BẢN
    if kq1!=None and not '{' in line:
        #print('TH_a')
        id=kq1.group(1).replace(' ','')
        type='group'
        parent='.'.join(id.split('.')[:-1])

        current_group=id #outcome dua vao de lay parent
        current_id=id #outcome dua vao de lay id =>1.2.3
        index_char=0 #outcome dua vao de lay id => a,b,c
        mastery_points=""
        ratings=",,,,,"
    #la group nhung ko co con => outcome
    elif kq1!=None and '{' in line:
        id=kq1.group(1).replace(' ','')
        type='outcome'
        parent='.'.join(id.split('.')[:-1])
        
        mastery_points="3"
        ratings="5,Tốt,3,Đạt,0,Không đạt"
    #1  KIẾN THỨC VÀ LẬP LUẬN NGÀNH
    elif kq1==None and kq2!=None and line.isupper():
        #print('TH_b')
        id=kq2.group(1).replace(' ','')
        type='group'
        parent=''
        mastery_points=""
        ratings=",,,,,"
        
    elif kq1==None and kq2==None and line.isupper()==False:
        #print('TH_c')
        char=chars[index_char]
        index_char+=1
        id='%s_%s'%(current_id,char)
        type='outcome'
        parent=current_group
        mastery_points="3"
        ratings="5,Tốt,3,Đạt,0,Không đạt"
    else:
        continue
        


    #xu ly ten mon hoc
    name=line
    name=line.replace('\r','').replace('\t','').replace('   ','')
    name=name.replace("  ",'')
    name=name.replace(",",'__COMMA__')
    name=name.replace(id,'')
    name=''.join(e for e in name if e.isalnum() or e==" " or e=="(" or e==")" or e=="{" or e=="}" or e=='_' or e=='.' or e=='-')
    
    if name=="" or name==" ":
        continue
    if name[0]==" ":
        name=name[1:]
    if name[0]==" ":
        name=name[1:]
    if name[0]==" ":
        name=name[1:]
       
    

    print("line:",line)
    print("id:",id)
    print("type:",type)
    print("parent:",parent)
    print("name:",name)
    #input('------------------------------------------------')
    #print('------------------------------------------------')
    
    if type=="group":
        nd_line="%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(id,type,id.replace('_','.')+' '+name,'',id,'','','',parent,mastery_points,ratings)
    else:
        nd_line="%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(id,type,id.replace('_','.'),name,id,'','','',parent,mastery_points,ratings)
    #nd_line="vendor_guid,object_type,title,description,display_name,calculation_method,calculation_int,workflow_state,parent_guids,mastery_points,ratings"

    
    writeUtf8('kq.txt',nd_line)
f.close()