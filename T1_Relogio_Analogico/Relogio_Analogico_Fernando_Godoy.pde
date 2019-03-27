void setup () {
  size(1000,1000);
  //rectMode(CENTER);
}

void draw () {
  float raio = 0.45*width;
  float raioPontosSegundos = raio*0.98;
  float raioPontosMinutos = raio*0.95;
  float raioPontosHoras = raio*0.92;
  float raioSegundos = raio*0.90;
  float raioMinutos = raio*0.70;
  float raioHoras = raio*0.40;
  float anguloSegundos = (second() * (PI/30)) - (PI/2);
  float anguloMinutos = (((minute()*60)+second()) * (PI/1800) ) - (PI/2);
  float anguloHoras = (((hour()*3600) + ((minute() * 60) + second())) * (PI/21600)) - (PI/2);
  
  background(255,255,255);
  translate(width/2, height/2);
  
  beginShape();
    
    
    ellipse(0,0,2*raio,2*raio);
    ellipse(0,0,2*raioPontosHoras,2*raioPontosHoras);
    stroke(255,0,0);
    line(0,0,raioSegundos*cos(TWO_PI+anguloSegundos),raioSegundos*sin(TWO_PI+anguloSegundos));
    stroke(0);
    strokeWeight(2);
    line(0,0,raioMinutos*cos(TWO_PI+anguloMinutos),raioMinutos*sin(TWO_PI+anguloMinutos));
    strokeWeight(3);
    line(0,0,raioHoras*cos(TWO_PI+anguloHoras),raioHoras*sin(TWO_PI+anguloHoras));
    strokeWeight(1);
    
    for(int angulo = 0; angulo <= 360; angulo++){

      float anguloRadSegundos = ((angulo) * (PI/150));
      float anguloRadMinutos = (angulo*(PI/30));
      float anguloRadHoras = (angulo*(PI/6)) - (PI/2);
      
      line(raioPontosMinutos*cos(anguloRadMinutos),raioPontosMinutos*sin(anguloRadMinutos),raio*cos(anguloRadMinutos),raio*sin(anguloRadMinutos));
      line(raioPontosHoras*cos(anguloRadHoras),raioPontosHoras*sin(anguloRadHoras),raio*cos(anguloRadHoras),raio*sin(anguloRadHoras));
      line(raioPontosSegundos*cos(anguloRadSegundos),raioPontosSegundos*sin(anguloRadSegundos),raio*cos(anguloRadSegundos),raio*sin(anguloRadSegundos));

      /*fill(255,0,0);
      text("palavra",raioPontosHoras*cos(anguloRadHoras),raioPontosHoras*sin(anguloRadHoras));
      noFill();*/
  }
  
    fill(255,0,0);
    stroke(255,0,0);
    ellipse(0,0,12,12);
    stroke(0);
    noFill();
    //ellipse(0,0,raioPontosSegundos,raioPontosSegundos);
    //ellipse(0,0,raioPontosMinutos,raioPontosMinutos);
    //ellipse(0,0,raioPontosHoras,raioPontosHoras);
   
  endShape(CLOSE);


}
