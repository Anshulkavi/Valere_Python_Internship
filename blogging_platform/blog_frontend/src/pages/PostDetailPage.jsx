import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import {
  Heart,
  Edit,
  User,
  Calendar,
  Tag,
  ArrowLeft,
  MessageSquare,
  Trash2,
  Share2,
  Check
} from "lucide-react";
import { postsAPI } from "../api/posts";
import { useAuth } from "../hooks/useAuth";
import LoadingSpinner from "../components/common/LoadingSpinner";
import { formatDateLong, formatTimeAgo } from "../utils/helpers";

const PostDetailPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { user } = useAuth();

  // State for post, comments, and loading
  const [post, setPost] = useState(null);
  const [comments, setComments] = useState([]);
  const [loading, setLoading] = useState(true);

  // State for the new comment form
  const [newComment, setNewComment] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  //New state for the share button's "Copied!" feedback
  const [copied, setCopied] = useState(false);

  // Fetch post and comments when the component loads or ID changes
  useEffect(() => {
    const fetchPostAndComments = async () => {
      try {
        setLoading(true);
        const [postData, commentsData] = await Promise.all([
          postsAPI.getPost(id),
          postsAPI.getCommentsForPost(id),
        ]);
        setPost(postData);
        setComments(commentsData);
      } catch (error) {
        console.error("Failed to fetch post or comments:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchPostAndComments();
  }, [id]);

  // Handler for the optimistic "like" update
  const handleLike = async () => {
    if (!user) {
      navigate("/login");
      return;
    }
    const originalPost = { ...post };
    setPost((currentPost) => ({
      ...currentPost,
      is_liked: !currentPost.is_liked,
      likes_count: currentPost.is_liked
        ? currentPost.likes_count - 1
        : currentPost.likes_count + 1,
    }));
    try {
      await postsAPI.likePost(id);
    } catch (error) {
      console.error("Failed to like post, reverting UI:", error);
      setPost(originalPost);
      alert("Something went wrong, please try liking again.");
    }
  };

  // Handler for submitting a new comment
  const handleCommentSubmit = async (e) => {
    e.preventDefault();
    if (!newComment.trim()) return;

    setIsSubmitting(true);
    try {
      await postsAPI.createComment(id, { content: newComment });
      setNewComment(""); // Clear the input field
      // Re-fetch comments to show the new one
      const commentsData = await postsAPI.getCommentsForPost(id);
      setComments(commentsData);
    } catch (error) {
      console.error("Failed to post comment:", error);
      alert("Could not post comment. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  // Handler for deleting a comment
  const handleCommentDelete = async (commentId) => {
    if (window.confirm("Are you sure you want to delete this comment?")) {
      try {
        await postsAPI.deleteComment(commentId);
        // Instantly remove the comment from the UI
        setComments((currentComments) =>
          currentComments.filter((comment) => comment.id !== commentId)
        );
      } catch (error) {
        console.error("Failed to delete comment:", error);
        alert("Could not delete the comment. Please try again.");
      }
    }
  };

  const handleShare = async () => {
        const shareData = {
            title: post.title,
            text: `Check out this post: ${post.title}`,
            url: window.location.href,
        };

        if (navigator.share) {
            try {
                await navigator.share(shareData);
            } catch (err) {
                console.error('Share failed:', err);
            }
        } else {
            // Fallback for browsers that do not support Web Share API
            navigator.clipboard.writeText(window.location.href);
            setCopied(true);
            setTimeout(() => setCopied(false), 2000); // Reset after 2 seconds
        }
    };

  // --- Render Logic ---

  if (loading) return <LoadingSpinner />;

  if (!post) {
    return (
      <div className="text-center py-20">
        <h1 className="text-2xl font-bold">Post not found</h1>
        <Link
          to="/"
          className="text-blue-600 hover:underline mt-4 inline-block"
        >
          Go back to Home
        </Link>
      </div>
    );
  }

  const authorName = post.author?.profile?.full_name || "Anonymous";
  const authorProfilePic = post.author?.profile?.profile_picture;

  return (
    <article className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <header className="mb-8">
        {post.category && (
          <p className="text-base font-semibold text-blue-600 uppercase tracking-wide">
            {post.category}
          </p>
        )}
        <h1 className="text-3xl md:text-5xl font-extrabold text-gray-900 mt-2 mb-4 leading-tight">
          {post.title}
        </h1>
        <div className="flex items-center space-x-4">
          <img
            src={
              authorProfilePic ||
              `https://ui-avatars.com/api/?name=${authorName.replace(
                /\s/g,
                "+"
              )}&background=random`
            }
            alt={authorName}
            className="w-12 h-12 rounded-full object-cover"
          />
          <div>
            <p className="font-semibold text-gray-800">{authorName}</p>
            <div className="flex items-center space-x-2 text-sm text-gray-500">
              <Calendar className="w-4 h-4" />
              <span>{formatDateLong(post.created_at)}</span>
            </div>
          </div>
        </div>
      </header>

      <div className="flex items-center justify-between border-y border-gray-200 py-3 mb-8">
        <div className="flex items-center space-x-3">
          <button
            onClick={handleLike}
            className={`flex items-center space-x-2 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
              post.is_liked
                ? "bg-red-100 text-red-700"
                : "bg-gray-100 text-gray-700 hover:bg-gray-200"
            } ${!user ? "cursor-not-allowed opacity-60" : ""}`}
          >
            <Heart
              className={`w-5 h-5 ${post.is_liked ? "fill-current" : ""}`}
            />
            <span>{post.likes_count || 0} Likes</span>
          </button>
          {user && user.id === post.author?.id && (
            <Link
              to={`/edit/${post.id}`}
              className="flex items-center space-x-2 px-3 py-2 bg-blue-100 text-blue-700 text-sm font-medium rounded-lg hover:bg-blue-200 transition-colors"
            >
              <Edit className="w-4 h-4" />
              <span>Edit</span>
            </Link>
          )}
          <button
                    onClick={handleShare}
                    className="flex items-center space-x-2 px-3 py-2 bg-gray-100 text-gray-700 text-sm font-medium rounded-lg hover:bg-gray-200 transition-colors"
                >
                    {copied ? <Check className="w-4 h-4 text-green-600" /> : <Share2 className="w-4 h-4" />}
                    <span>{copied ? 'Copied!' : 'Share'}</span>
                </button>
        </div>
      </div>

      {post.featured_image && (
        <img
          src={post.featured_image}
          alt={post.title}
          className="w-full h-auto max-h-[500px] object-cover rounded-xl mb-8 shadow-lg"
        />
      )}

      <div className="prose prose-lg max-w-none text-gray-800 leading-relaxed whitespace-pre-wrap">
        {post.content}
      </div>

      {post.tags && post.tags.length > 0 && (
        <div className="mt-10 pt-6 border-t border-gray-200">
          <h3 className="text-sm font-semibold text-gray-600 uppercase mb-3">
            Tags
          </h3>
          <div className="flex flex-wrap gap-3">
            {post.tags.map((tag) => (
              <span
                key={tag}
                className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800"
              >
                <Tag className="w-4 h-4 mr-2 text-gray-500" />
                {tag}
              </span>
            ))}
          </div>
        </div>
      )}

      <div className="mt-12 pt-8 border-t border-gray-200">
        <h2 className="text-2xl font-bold text-gray-900 mb-6 flex items-center">
          <MessageSquare className="w-6 h-6 mr-3" />
          Comments ({comments.length})
        </h2>
        {user ? (
          <form onSubmit={handleCommentSubmit} className="mb-8">
            <textarea
              value={newComment}
              onChange={(e) => setNewComment(e.target.value)}
              placeholder="Write a comment..."
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
              rows="3"
              required
            />
            <button
              type="submit"
              disabled={isSubmitting}
              className="mt-3 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50"
            >
              {isSubmitting ? "Posting..." : "Post Comment"}
            </button>
          </form>
        ) : (
          <div className="mb-8 p-4 bg-gray-100 rounded-lg text-center">
            <p>
              Please{" "}
              <Link to="/login" className="text-blue-600 font-semibold">
                log in
              </Link>{" "}
              to post a comment.
            </p>
          </div>
        )}
        {/* // Replace the existing comments section with this one */}
        <div className="space-y-6">
          {comments.length > 0 ? (
            comments.map((comment) => {
              // --- START OF DEBUGGING BLOCK ---
              const loggedInUserId = user ? Number(user.id) : null;
              const commentAuthorId = Number(comment.user_id);
              const postAuthorId = user ? Number(post.author?.id) : null;

              const isCommentAuthor = loggedInUserId === commentAuthorId;
              const isPostAuthor = loggedInUserId === postAuthorId;
              const shouldShowDeleteButton =
                user && (isCommentAuthor || isPostAuthor);

              console.log(
                `%c--- Analyzing Comment ID: ${comment.id} ---`,
                "font-weight: bold; color: blue; font-size: 14px;",
                "\nLogged-in User ID:",
                loggedInUserId,
                `(Type: ${typeof loggedInUserId})`,
                "\nComment Author ID:",
                commentAuthorId,
                `(Type: ${typeof commentAuthorId})`,
                "\nPost Author ID:",
                postAuthorId,
                `(Type: ${typeof postAuthorId})`,
                "\n\nIs User the Comment Author?",
                isCommentAuthor,
                "\nIs User the Post Author?",
                isPostAuthor,
                "\n===> Should Delete Button Show?",
                shouldShowDeleteButton,
                "\n--------------------"
              );
              // --- END OF DEBUGGING BLOCK ---

              return (
                <div key={comment.id} className="flex space-x-4">
                  <div className="w-10 h-10 bg-gray-200 rounded-full flex-shrink-0 flex items-center justify-center">
                    <User className="w-5 h-5 text-gray-600" />
                  </div>
                  <div className="flex-grow">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="font-semibold">{comment.user_name}</p>
                        <p className="text-xs text-gray-500">
                          {formatTimeAgo(comment.created_at)}
                        </p>
                      </div>

                      {/* This is the button logic that uses our debug variables */}
                      {shouldShowDeleteButton && (
                        <button
                          onClick={() => handleCommentDelete(comment.id)}
                          title="Delete comment"
                          className="text-gray-400 hover:text-red-600 transition-colors"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      )}
                    </div>
                    <p className="text-gray-700 mt-1 whitespace-pre-wrap">
                      {comment.content}
                    </p>
                  </div>
                </div>
              );
            })
          ) : (
            <p className="text-gray-600">
              No comments yet. Be the first to comment!
            </p>
          )}
        </div>
      </div>

      <footer className="mt-12 pt-8 border-t border-gray-200">
        <Link
          to="/"
          className="inline-flex items-center font-medium text-blue-600 hover:text-blue-800 transition-colors"
        >
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back to all posts
        </Link>
      </footer>
    </article>
  );
};

export default PostDetailPage;
