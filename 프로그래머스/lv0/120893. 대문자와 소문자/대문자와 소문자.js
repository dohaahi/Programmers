function solution(my_string) {
    var result = '';
    
    for (sen of my_string) {
        if( sen == sen.toLowerCase()) {
            result += sen.toUpperCase()
        } else {
            result += sen.toLowerCase()
        }
    }
    
    return result;
}