from b3desk.commands import bp


def test_api_meetings_for_user_can_use_sip_in_group_enable_sip_and_setting_enable_sip(
    client_app,
    user,
    user_2,
    meeting,
    meeting_2,
    meeting_3,
    meeting_1_user_2,
    shadow_meeting,
    iam_token,
    group,
    group_2,
    group_3,
    authenticated_user,
):
    """Test that API returns SIPMediaGW_url if meeting's owner in group 1: enable sip, 2: disable sip, 3: none able sip and settings enable sip."""
    res = client_app.get("/admin/manage-group-members/1", status=200)
    res.form["search"] = "alice@domain.tld"
    res = res.form.submit()
    res = client_app.get(
        "/api/meetings", headers={"Authorization": f"Bearer {iam_token.access_token}"}
    )
    assert (
        res.json["meetings"][0]["SIPMediaGW_url"]
        == res.json["meetings"][0]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert (
        res.json["meetings"][1]["SIPMediaGW_url"]
        == res.json["meetings"][1]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert (
        res.json["meetings"][2]["SIPMediaGW_url"]
        == res.json["meetings"][2]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert (
        res.json["meetings"][3]["SIPMediaGW_url"]
        == res.json["meetings"][3]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert res.json["meetings"][3]["delegate"]


def test_api_meetings_for_delegate_can_use_sip_and_owner_none_able_to_use_sip(
    cli_runner,
    client_app,
    user,
    user_2,
    meeting,
    meeting_2,
    meeting_3,
    meeting_1_user_2,
    shadow_meeting,
    iam_token,
    group,
    group_2,
    group_3,
    authenticated_user,
):
    """Test that API returns not SIPMediaGW_url if meeting's owner in group 2: disable sip, 3: none able sip and settings enable sip."""
    cli_runner.invoke(bp.cli, ["user-to-admin", "alice@domain.tld"])
    res = client_app.get("/admin/manage-group-members/2", status=200)
    res.form["search"] = "berenice@domain.tld"
    res = res.form.submit()
    res = client_app.get("/admin/manage-group-members/3", status=200)
    res.form["search"] = "berenice@domain.tld"
    res = res.form.submit()
    assert user_2.groups[0].name == "Group 2"
    assert user_2.groups[1].name == "Group 3"
    res = client_app.get(
        "/api/meetings", headers={"Authorization": f"Bearer {iam_token.access_token}"}
    )
    assert (
        res.json["meetings"][0]["SIPMediaGW_url"]
        == res.json["meetings"][0]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert (
        res.json["meetings"][1]["SIPMediaGW_url"]
        == res.json["meetings"][1]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert (
        res.json["meetings"][2]["SIPMediaGW_url"]
        == res.json["meetings"][2]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert (
        res.json["meetings"][3]["SIPMediaGW_url"]
        == res.json["meetings"][3]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert res.json["meetings"][3]["delegate"]


def test_api_meetings_for_delegate_can_use_sip_and_owner_cannot(
    cli_runner,
    client_app,
    user,
    user_2,
    meeting,
    meeting_2,
    meeting_3,
    meeting_1_user_2,
    shadow_meeting,
    iam_token,
    group,
    group_2,
    group_3,
    authenticated_user,
):
    """Test that API returns not SIPMediaGW_url if meeting's owner in group 2: disable sip, 3: disable sip and settings enable sip."""
    cli_runner.invoke(bp.cli, ["user-to-admin", "alice@domain.tld"])
    res = client_app.get("/admin/manage-group-members/2", status=200)
    res.form["search"] = "berenice@domain.tld"
    res = res.form.submit()
    res = client_app.get("/admin/manage-group-members/3", status=200)
    res.form["search"] = "berenice@domain.tld"
    res = res.form.submit()
    res = client_app.get("/admin/edit-group/3", status=200)
    res.form["enable_sip"] = False
    res.form.submit()
    assert user_2.groups[0].name == "Group 2"
    assert user_2.groups[1].name == "Group 3"
    res = client_app.get(
        "/api/meetings", headers={"Authorization": f"Bearer {iam_token.access_token}"}
    )
    assert (
        res.json["meetings"][0]["SIPMediaGW_url"]
        == res.json["meetings"][0]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert (
        res.json["meetings"][1]["SIPMediaGW_url"]
        == res.json["meetings"][1]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert (
        res.json["meetings"][2]["SIPMediaGW_url"]
        == res.json["meetings"][2]["visio_code"]
        + "@"
        + client_app.app.config["FQDN_SIP_SERVER"]
    )
    assert "SIPMediaGW_url" not in res.json["meetings"][3]
    assert res.json["meetings"][3]["delegate"]
