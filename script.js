document.addEventListener('DOMContentLoaded', () => {
    // Año actual en el pie de página
    const anioActual = document.getElementById('anio-actual');
    if (anioActual) anioActual.textContent = new Date().getFullYear();

    // Alternar menú móvil
    const alternarMenu = document.querySelector('.alternar-menu');
    const enlacesNav = document.querySelector('.enlaces-nav');
    const enlaces = document.querySelectorAll('.enlaces-nav li');

    alternarMenu.addEventListener('click', () => {
        enlacesNav.classList.toggle('activo');
        alternarMenu.classList.toggle('activo');
    });

    // Cerrar menú al hacer clic en un enlace
    enlaces.forEach(enlace => {
        enlace.addEventListener('click', () => {
            enlacesNav.classList.remove('activo');
            alternarMenu.classList.remove('activo');
        });
    });

    // Animaciones de desplazamiento usando Intersection Observer
    const opcionesObservador = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observador = new IntersectionObserver((entradas) => {
        entradas.forEach(entrada => {
            if (entrada.isIntersecting) {
                entrada.target.classList.add('mostrar');
                observador.unobserve(entrada.target); // Solo animar una vez
            }
        });
    }, opcionesObservador);

    const elementosOcultos = document.querySelectorAll('.oculto, .anim-aparecer-arriba');
    elementosOcultos.forEach(el => observador.observe(el));

    // Efecto de desplazamiento de la barra de navegación
    const barraNavegacion = document.querySelector('.barra-navegacion');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            barraNavegacion.style.background = 'rgba(31, 32, 65, 0.95)';
            barraNavegacion.style.boxShadow = '0 4px 6px -1px rgba(17, 157, 164, 0.1)';
        } else {
            barraNavegacion.style.background = 'rgba(31, 32, 65, 0.8)';
            barraNavegacion.style.boxShadow = 'none';
        }
    });
});
