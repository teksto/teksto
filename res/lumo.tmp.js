function fls(dat, prt= '#EDT', opt= false){
  const f= dat[0];
  const B= new Blob([dat]);
  const R= new FileReader();

  const lk= document.createElement('a');
    lk.style.display= 'none';
    lk.download= 'NUL.json';
    lk.href= URL.createObjectURL(B);
    
  function savi(){console.log('savi',kk)}

  function legu(){console.log(f)}
    // R.onload= function(){
    //   // console.log(this.result)
    //   // return JSON.parse(f.target.result)
    //   // return this.result
    //   document.querySelector(prt).innerText= this.result
    // }
    // R.readAsText(f, 'utf-8')
  opt? savi() : legu();
}