document.addEventListener("DOMContentLoaded", () => {
    const grid = document.querySelector(".grid");
    const sidebar = document.getElementById("sidebar");
    const wrapper = document.querySelector(".gallery-wrapper");

    // Apply correct margin before any layout
    if (sidebar && wrapper) {
        const isCollapsed = sidebar.classList.contains("collapsed");
        wrapper.style.marginLeft = isCollapsed ? "0" : "250px";
    }

    // Wait for all images to be fully loaded and DOM to settle
    imagesLoaded(grid, () => {
        window.msnry = new Masonry(grid, {
            itemSelector: ".grid-item",
            columnWidth: ".grid-sizer",
            percentPosition: true,
            gutter: 0,
        });

        // Do a second layout after a tiny delay to ensure everything snaps
        setTimeout(() => {
            if (window.msnry) window.msnry.layout();
        }, 100);
    });

    // Sidebar toggle logic
    const toggleBtn = document.getElementById("sidebar-toggle");
    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            const isCollapsed = sidebar.classList.toggle("collapsed");
            wrapper.style.marginLeft = isCollapsed ? "0" : "250px";
            document.body.classList.toggle("sidebar-visible", !isCollapsed);
            setTimeout(() => {
                if (window.msnry) window.msnry.layout();
            }, 350);
        });
    }

    // Filter handling (unchanged)
    const checkboxes = document.querySelectorAll('#tag-filter input[type="checkbox"]');
    checkboxes.forEach(checkbox =>
        checkbox.addEventListener("change", () => {
            const activeTags = Array.from(checkboxes)
                .filter(cb => cb.checked)
                .map(cb => cb.value.toLowerCase());

            updateURLFromFilters(activeTags);
            applyTagFilter(activeTags);
        })
    );

    if (document.getElementById('clear-filters')) {
        document.getElementById('clear-filters').addEventListener('click', () => {
            document.querySelectorAll('#tag-filter input[type="checkbox"]').forEach(cb => cb.checked = false);
            document.querySelectorAll('.grid-item').forEach(item => item.style.display = 'block');
            if (window.msnry) window.msnry.layout();
            updateURLFromFilters([]);
        });
    }

    syncFiltersWithURL();
});


function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const wrapper = document.querySelector('.gallery-wrapper');
    const isCollapsed = sidebar.classList.toggle('collapsed');

    // Adjust gallery margin manually
    if (wrapper) {
        wrapper.style.marginLeft = isCollapsed ? '0' : '250px';
    }

    document.body.classList.toggle('sidebar-visible', !isCollapsed);

    // Wait a bit and reflow grid
    setTimeout(() => {
        if (window.msnry) window.msnry.layout();
    }, 350);
}



function updateURLFromFilters(activeTags) {
    const params = new URLSearchParams(window.location.search);
    if (activeTags.length > 0) {
        params.set('tags', activeTags.join(','));
    } else {
        params.delete('tags');
    }
    const newUrl = window.location.pathname + '?' + params.toString();
    history.replaceState(null, '', newUrl);
}

function applyTagFilter(activeTags) {
    document.querySelectorAll(".grid-item").forEach(item => {
        const tags = item.dataset.tags.toLowerCase().split(" ");
        const show = activeTags.length === 0 || activeTags.every(tag => tags.includes(tag));
        item.style.display = show ? "block" : "none";
    });
    if (window.msnry) window.msnry.layout();
}

function syncFiltersWithURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const tagParam = urlParams.get('tags');
    const activeTags = tagParam ? tagParam.toLowerCase().split(',') : [];

    const checkboxes = document.querySelectorAll('#tag-filter input[type="checkbox"]');
    checkboxes.forEach(cb => {
        cb.checked = activeTags.includes(cb.value.toLowerCase());
    });

    applyTagFilter(activeTags);
}

