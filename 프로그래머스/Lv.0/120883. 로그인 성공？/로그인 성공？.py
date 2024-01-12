def solution(id_pw, db):
    for id,pw in db:
        if id != id_pw[0]:
            continue
        
        if pw == id_pw[1]:
            return "login"
        
        return "wrong pw" 
    return "fail"