#!/usr/bin/env python3.7

import iterm2
# This script was created with the "basic" environment which does not support adding dependencies
# with pip.

async def main(connection):
    await iterm2.Window.async_create(connection)
    app = await iterm2.async_get_app(connection)

    # Create split panes and make the bottom left one active.
    bottomLeft = app.current_terminal_window.current_tab.current_session
    bottomCenter = await bottomLeft.async_split_pane(vertical=True,before=False)
    bottomRight = await bottomCenter.async_split_pane(vertical=True)
    middleLeft = await bottomLeft.async_split_pane(vertical=False,before=True)
    middleCenter = await bottomCenter.async_split_pane(vertical=False,before=True)
    middleRight = await bottomRight.async_split_pane(vertical=False,before=True)
    topLeft = await middleLeft.async_split_pane(vertical=False, before=True)
    topCenter = await middleCenter.async_split_pane(vertical=False,before=True)
    topRight = await middleRight.async_split_pane(vertical=False, before=True)

    await bottomLeft.async_activate()
    await bottomLeft.async_send_text("bottomLeft\n", suppress_broadcast=True)
    await bottomCenter.async_send_text("bottomCenter\n", suppress_broadcast=True)
    await bottomRight.async_send_text("bottomRight\n", suppress_broadcast=True)
    await middleLeft.async_send_text("middleLeft\n", suppress_broadcast=True)
    await middleCenter.async_send_text("middleCenter\n", suppress_broadcast=True)
    await middleRight.async_send_text("middleRight\n", suppress_broadcast=True)
    await topLeft.async_send_text("topLeft\n", suppress_broadcast=True)
    await topCenter.async_send_text("topCenter\n", suppress_broadcast=True)
    await topRight.async_send_text("topRight\n", suppress_broadcast=True)
    
    await topLeft.async_send_text("exit\n", suppress_broadcast=True)
    await middleLeft.async_send_text("ssh svr-media-01.tcudelocal.net\n", suppress_broadcast=True)
    await bottomLeft.async_send_text("ssh svr-pykms-01.tcudelocal.net\n", suppress_broadcast=True)
    await topCenter.async_send_text("ssh svr-adguard-01.tcudelocal.net\n", suppress_broadcast=True)
    await middleCenter.async_send_text("ssh svr-adguard-02.tcudelocal.net\n", suppress_broadcast=True)
    await bottomCenter.async_send_text("ssh svr-librenms-01.tcudelocal.net\n", suppress_broadcast=True)
    await topRight.async_send_text("ssh svr-monitoring-01.tcudelocal.net\n", suppress_broadcast=True)
    await middleRight.async_send_text("exit\n", suppress_broadcast=True)
    await bottomRight.async_send_text("exit\n", suppress_broadcast=True)

    broadcast_to = [  middleLeft, bottomLeft, topCenter, middleCenter, bottomCenter,  topRight  ]
    for session in broadcast_to:
        await session.async_send_text("cd /home/tcude/docker && ls -lah\n")

iterm2.run_until_complete(main)
