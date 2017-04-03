console.log("Ye");

window.onload = () => {
    // this is incredibly memory intensive
    // var yeezyGifs = ["https://media.giphy.com/media/aI6O9VZvuTe36/giphy.gif",
    //                  "https://images.rapgenius.com/1cadcf22f782de99f0c5e449aca5eb17.500x281x29.gif",
    //                  "https://i0.wp.com/fusion.net/wp-content/uploads/2015/08/tumblr_nnbg84ml4a1sxv3djo1_500.gif?resize=500%2C280&quality=80&strip=all"];
    // var yeezyCount = 0;
    // setInterval(() => {
    //     yeezyCount = (yeezyCount++ == 2) ? 0 : yeezyCount;
    //     $("body").css("background-image", `url(${yeezyGifs[yeezyCount]})`);
    // }, 2000);

    $("body").mousemove((e) => {
        $(".mouse-follow").css({
            top: `${e.pageY}px`,
            left: `${e.pageX}px`
        });
    });
}