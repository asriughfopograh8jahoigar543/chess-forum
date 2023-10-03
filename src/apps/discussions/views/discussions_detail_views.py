from django.shortcuts import redirect, render
from django.views import View

from discussions.forms.reply_forms import ReplyForm
from discussions.services.discussion_service import DiscussionService
from discussions.services.reply_service import ReplyService
from discussions.services.reply_like_service import ReplyLikeService

class DiscussionListView(View):
    def get(self, request):
        discussions = DiscussionService.get_all_discussions()
        return render(request, "discussions/discussion_list.html", {"discussions": discussions})

class DiscussionDetailView(View):
    def get(self, request, discussion_id):
        discussion = DiscussionService.get_discussion_by_id(discussion_id)
        replies = ReplyService.get_replies_for_discussion(discussion)
        reply_form = ReplyForm()
        return render(
            request,
            "discussions/discussion_detail.html",
            {"discussion": discussion, "replies": replies, "reply_form": reply_form},
        )

    def post(self, request, discussion_id):
        discussion = DiscussionService.get_discussion_by_id(discussion_id)
        replies = ReplyService.get_replies_for_discussion(discussion)
        reply_form = ReplyForm()

        if request.method == "POST":
            reply_form = ReplyForm(request.POST, request.FILES)
            if reply_form.is_valid():
                ReplyService.create_reply(discussion, request.user, reply_form.cleaned_data)
                return redirect("discussion_detail", discussion_id=discussion_id)

            if "like_reply" in request.POST:
                reply_id = request.POST["like_reply"]
                reply_to_like = ReplyService.get_reply_by_id(reply_id)
                ReplyLikeService.toggle_like(request.user, reply_to_like)

            if "close_discussion" in request.POST and request.user == discussion.author:
                DiscussionService.close_discussion(discussion)

        return render(
            request,
            "discussions/discussion_detail.html",
            {"discussion": discussion, "replies": replies, "reply_form": reply_form},
        )


