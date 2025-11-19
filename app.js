gsap.from(".title", {duration:1, y:-50, opacity:0});
gsap.from(".btn", {duration:1, scale:0, stagger:0.2});

const canvas = document.getElementById('heartCanvas');
if(canvas){
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight,0.1,1000);
    const renderer = new THREE.WebGLRenderer({canvas:canvas,alpha:true});
    renderer.setSize(window.innerWidth,window.innerHeight);
    camera.position.z = 5;

    const loader = new THREE.FontLoader();
    const hearts = [];

    loader.load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', function(font){
        for(let i=0;i<20;i++){
            const textGeo = new THREE.TextGeometry("❤️", {font:font,size:0.5,height:0.1});
            const textMat = new THREE.MeshBasicMaterial({color:0xff69b4});
            const textMesh = new THREE.Mesh(textGeo,textMat);
            textMesh.position.set((Math.random()-0.5)*10,(Math.random()-0.5)*10,(Math.random()-0.5)*10);
            textMesh.rotation.set(Math.random()*2,Math.random()*2,0);
            scene.add(textMesh);
            hearts.push(textMesh);
        }
    });

    function animate(){
        requestAnimationFrame(animate);
        hearts.forEach(h=>{
            h.rotation.y += 0.01;
            h.position.y -= 0.01;
            if(h.position.y < -5) h.position.y = 5;
        });
        renderer.render(scene,camera);
    }
    animate();
}