function ae(a=1,b,c){
  this.a=a;
  this.b=b;
  this.c=c;

  // console.log(a,b,c)
  this.ll= function(){return 999}
}

function lumo({
  a=1, b=2, c=3
}){
  return { a,b,c};
}