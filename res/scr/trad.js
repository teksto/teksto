// Trad zh2tg


// json 模糊查询
function fuzzy(d,o,v){
  const r= d.filter(e=> e[o].includes(v));
  return r
}

function fuzzyQuery(index){
  if(index == "" || index == null){
    json= eval(dj); return json
  }else{
    njson= [];
    json= eval(dj);
    for(let i=0; i<json.length; i++){
      if( (json[i].Interpreto).indexOf(index) > -1 ){
        const tjson= {
          nb: i,
          id: json[i].Seria,
          tt: json[i].Interpreto
        }
        njson.push(tjson)
      }
    }
    return njson
  }
}