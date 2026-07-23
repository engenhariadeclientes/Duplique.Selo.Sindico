function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var dados = JSON.parse(e.postData.contents);

  sheet.appendRow([
    new Date(),
    dados.nome || "",
    dados.email || "",
    dados.telefone || "",
    dados.cidade || "",
    dados.estado || "",
    dados.perfil || "",
    dados.qtdCondominios || "",
    dados.qtdUnidades || "",
    dados.tipoCobranca || "",
    dados.score || "",
    dados.nivel || ""
  ]);

  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}
