$('#region').on('change', function () {
	const regionid = parseInt($(this).val());
	$('#comuna option').hide();
    $("#comuna").val("0");

	if (regionid !== 0) {
		$('#comuna option').each(function () {
			const comuna_region_id = parseInt($(this).attr('regionid'));
			if (comuna_region_id === regionid) {
				$(this).show();
			}
		});
	}
});

