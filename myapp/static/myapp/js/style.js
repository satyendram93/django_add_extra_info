$(document).ready(function() {
    $("#add-field-btn").click(function() {
        let fieldHTML = `
            <div class="extra-fields mb-3">
                <input type="text" name="extra_key[]" class="form-control mt-1" placeholder="Key" required>
                <input type="text" name="extra_value[]" class="form-control mt-1" placeholder="Value" required>
                <button type="button" class="remove-btn mt-1" style="background: gray; color: white; padding: 5px 10px; border: none; cursor: pointer;">❌</button>
            </div>`;
        $("#extra-fields-container").append(fieldHTML);
    });

    $(document).on("click", ".remove-btn", function() {
        $(this).closest(".extra-fields").remove();
    });
});