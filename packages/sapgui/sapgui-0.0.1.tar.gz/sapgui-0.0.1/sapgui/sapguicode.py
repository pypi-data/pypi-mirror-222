def zmpua25(session, *args):
    """
    Function to run zmpua25 code.
    :param session: parameter obtained from sapgui.
    :param args: variant:str, material_id: DataFrame
    :return: none.
    """
    session.findById("wnd[0]").maximize()
    session.findById("wnd[0]/tbar[0]/okcd").text = "ZMPUA25"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/tbar[1]/btn[17]").press()
    session.findById("wnd[1]/usr/txtV-LOW").text = args[0]
    session.findById("wnd[1]/usr/txtENAME-LOW").text = ""
    session.findById("wnd[1]/usr/txtV-LOW").caretPosition = 6
    session.findById("wnd[1]/tbar[0]/btn[8]").press()
    args[1].to_clipboard(index=False, header=None)
    session.findById(r"wnd[0]/usr/btn%_R_MATNR_%_APP_%-VALU_PUSH").press()
    session.findById("wnd[1]/tbar[0]/btn[16]").press()
    session.findById("wnd[1]/tbar[0]/btn[24]").press()
    session.findById("wnd[1]/tbar[0]/btn[8]").press()
