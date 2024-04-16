$(document).ready(function() {
    $(".doctor-link").click(function(event) {
        event.preventDefault(); 
        var doctorId = $(this).data('doctor-id');
        var url = '/chats/' + doctorId + '/consultations/';  

        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                var consultationList = $('#consultation-list');
                consultationList.empty();  

                if (response.consultations.length > 0) {
                    $.each(response.consultations, function(index, consultation) {
                        var consultationItem = `
                            <li>
                                <h3>${consultation.title}</h3>
                                <p>${consultation.description}</p>
                                <p>User ID: ${consultation.user_id}</p>
                            </li>`;
                        consultationList.append(consultationItem);
                    });
                } else {
                    consultationList.append('<li>No consultations found for this doctor.</li>');
                }
            },
            error: function(error) {
                console.error(error);
                // Handle error (display message, etc.)
            }
        });
    });
});