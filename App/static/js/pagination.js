
$(document).ready(function () {
    let currentPage = 1;

    function fetchopinions(page) {
        $.ajax({
            url: "{{ url_for('visit.get_opinions') }}",
            type: 'GET',
            data: { page: page },
            success: function (response) {
                $('#opinions-container').empty();
                if (response.opinions.length > 0) {
                    response.opinions.forEach(comment => {
                        $('#opinions-container').append(`
                <div class="list-group-item">
                  <small>
                    Calificación:
                    <span class="stars">
                      ${[...Array(5).keys()].map(i => i < comment.rating_product ? '<i class="fa fa-star checked"></i>' : '<i class="fa fa-star"></i>').join('')}
                    </span>
                    | Fecha: ${new Date(comment.date_opinion).toLocaleDateString('es-ES')}
                  </small>
                  <h5 class="mb-1">${comment.username_opinion}</h5>
                  <p class="mb-1">${comment.id_product}</p>
                  <p class="mb-1">${comment.comment_opinion}</p>
                </div>
              `);
                    });
                } else {
                    $('#opinions-container').append('<p class="text-center">No hay comentarios todavía.</p>');
                }
                updatePagination(response.page, response.total, response.per_page);
            }
        });
    }

    function updatePagination(page, total, perPage) {
        $('#pagination').empty();
        const totalPages = Math.ceil(total / perPage);
        for (let i = 1; i <= totalPages; i++) {
            $('#pagination').append(`
          <li class="page-item ${i === page ? 'active' : ''}">
            <a class="page-link" href="#" data-page="${i}">${i}</a>
          </li>
        `);
        }
    }

    $(document).on('click', '.page-link', function (e) {
        e.preventDefault();
        const page = $(this).data('page');
        if (page !== currentPage) {
            currentPage = page;
            fetchopinions(page);
        }
    });

    fetchopinions(currentPage);
});
