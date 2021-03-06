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

    # This contains many panes, some of which you may not want to utilize. If that is the case, proceed to the next block of code and change any existing command to `exit`

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

    # As mentioned previously, simply replace your `ssh` command with `exit` and the extra pane(s) will close immediately
    
    await topLeft.async_send_text("ssh svr-ansible-01.tcudelocal.net\n", suppress_broadcast=True)
    await middleLeft.async_send_text("ssh svr-media-01.tcudelocal.net\n", suppress_broadcast=True)
    await bottomLeft.async_send_text("ssh svr-pykms-01.tcudelocal.net\n", suppress_broadcast=True)
    await topCenter.async_send_text("ssh svr-adguard-01.tcudelocal.net\n", suppress_broadcast=True)
    await middleCenter.async_send_text("ssh svr-adguard-02.tcudelocal.net\n", suppress_broadcast=True)
    await bottomCenter.async_send_text("ssh svr-librenms-01.tcudelocal.net\n", suppress_broadcast=True)
    await topRight.async_send_text("ssh svr-monitoring-01.tcudelocal.net\n", suppress_broadcast=True)
    await middleRight.async_send_text("ssh svr-docker-external-01.tcudelocal.net\n", suppress_broadcast=True)
    await bottomRight.async_send_text("ssh svr-docker-internal-01.tcudelocal.net\n", suppress_broadcast=True)

    # This contains the command you'd like to be run once each pane is SSH'd into their respective host. Ensure the panes mentioned here are correct

    broadcast_to = [  middleLeft, middleRight, bottomRight  ]
    for session in broadcast_to:
        await session.async_send_text("cd /home/tcude/docker && ls -lah\n")

    broadcast_to = [  topLeft  ]
    for session in broadcast_to:
        await session.async_send_text("cd /home/tcude/ansible/scripts && ls -lah\n")

    broadcast_to = [  bottomLeft  ]
    for session in broadcast_to:
        await session.async_send_text("cd /home/tcude/docker/pykms && ls -lah\n")

    broadcast_to = [  topCenter  ]
    for session in broadcast_to:
        await session.async_send_text("cd /home/tcude/docker/adguard && ls -lah\n")

    broadcast_to = [  middleCenter  ]
    for session in broadcast_to:
        await session.async_send_text("cd /home/tcude/docker/adguard && ls -lah\n")

    broadcast_to = [  bottomCenter  ]
    for session in broadcast_to:
        await session.async_send_text("cd /home/tcude/docker/librenms && ls -lah\n")

    broadcast_to = [  topRight  ]
    for session in broadcast_to:
        await session.async_send_text("cd /home/tcude/docker/grafana_influxdb && ls -lah\n")

iterm2.run_until_complete(main)
