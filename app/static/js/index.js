const hero = document.querySelector(".hero");
const slider = document.querySelector('.slider');
const logo = document.querySelector('#logo');
const txtlogin = document.querySelector('#dangNhap');
const headline = document.querySelector('.headline');

const tl = new TimelineMax();

tl.fromTo(headline,1.2,
        {
            color:"#492dc5",
        },
        {
            color:"#FFFFFF",
        },0.2).fromTo(hero,1,
            {
                height: "0%"
            }, 
            {
                height: "80%",
                ease: Power2.easeInOut
            },0)
    .fromTo(hero,1.2,
        {
            width: "100%",
            marginLeft: "0px",
        }, 
        {
            marginLeft: "130px",
            width: "80%",
            ease: Power2.easeInOut
        },1
    ).fromTo(slider,1.2,
        { 
            x: "-100%"
        }, 
        {
            x: "0%",
            ease: Power2.easeInOut
        }
        ,"-=1.2"
    ).fromTo(logo,0.5,
        { 
            opacity: 0,
            x: 30
        }, 
        {
            opacity: 1,
            x: 0
        }
        ,"-=0.5"
    ).fromTo(txtlogin,0.5,
        { 
            opacity: 0,
            x: 30
        }, 
        {
            opacity: 1,
            x: 0
        }
        ,"-=0.3"
    );

$('.carousel').carousel({
  interval: 1
});