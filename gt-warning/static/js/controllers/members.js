angular.module('gtWarning')
    .controller('MemberCtrl', function ($scope, $rootScope, $http, $state) {
        $scope.allMembers = [
            {_id: "member1", level: 1},
            {_id: "m2", level: 21},
            {_id: "mme3", level: 3}
        ];
        $scope.newMember = {
            _id: "",
            email: "",
            tel: "",
            wechat: ""
        };
        $scope.aMember = {
            _id: "test-mongo",
            level: 10,
            note: "hehehe"
        };
        $scope.showPop = false;
        $scope.newMemberMessage = undefined;
        $scope.changeMemberMessage = undefined;
        $scope.setMember = function (member) {
            $scope.aMember = member;
            $scope.showPop = true;
            $scope.changeMemberMessage = false;
        };

        $scope.submitSetMember = function (member) {
            $scope.changeMemberMessage = undefined;
            $http.post("/api/members_change", member).success(function (data) {
                if (data.status == 1) {
                    $scope.changeMemberMessage = "member 修改成功";
                } else {
                    $scope.changeMemberMessage = "修改失败";
                }
            })
        };

        $scope.addMember = function (member) {
            $scope.newMemberMessage = false;
            if (!member._id) {
                $scope.newMemberMessage = "请填写member name";
                return;
            } else if (!member.email) {
                $scope.newMemberMessage = "请填写member email";
                return;
            } else if (!member.tel) {
                $scope.newMemberMessage = "请填写member 手机号";
                return;
            } else if (!member.wechat) {
                $scope.newMemberMessage = "请填写member 微信号";
                return;
            } else {
                $http.post("/api/members", member).success(function (data) {
                    if (data.status == 1) {
                        $scope.newMemberMessage = "member 添加成功!";
                        $scope.allMembers.push(member);
                    } else if (data.error) {
                        $scope.newMemberMessage = data.error;
                    } else {
                        $scope.newMemberMessage = "添加失败";
                    }                                   
                });
            }
        };

        var init = function () {
            $http.get("/api/members").success(function (data) {
                if (data.status == 1) {
                    $scope.allMembers = data.data;
                } else {
                    console.log("some err");
                }
            })
        };
        init();
    });