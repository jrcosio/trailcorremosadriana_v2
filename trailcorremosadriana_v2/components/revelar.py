import reflex as rx

_CSS = """
.reveal { opacity: 0; }
.reveal.visible { opacity: 1; animation: reveal-in 0.6s ease; }
@keyframes reveal-in {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}
@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1; }
  .reveal.visible { animation: none; }
}
"""

# El MutationObserver es necesario porque las cards de noticias se montan
# después, cuando llega el state del on_load por websocket.
_JS = """
(function() {
    const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
            if (e.isIntersecting) {
                e.target.classList.add('visible');
                io.unobserve(e.target);
            }
        });
    }, { threshold: 0.15 });

    function scan() {
        document.querySelectorAll('.reveal:not([data-rv])').forEach((el) => {
            el.dataset.rv = '1';
            io.observe(el);
        });
    }

    scan();
    new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
})();
"""


def efecto_revelar() -> rx.Component:
    """Estilo + script del reveal al hacer scroll. Incluir una vez por página;
    los elementos con class_name="reveal" aparecen al entrar en el viewport."""
    return rx.fragment(
        rx.el.style(_CSS),
        rx.script(_JS),
    )
