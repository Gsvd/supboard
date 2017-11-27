$(document).ready(function () {
    const twitter_block = document.querySelector('.twitter_block')
    const twitter_block_height = twitter_block.scrollHeight - twitter_block.offsetHeight
    var scroll_direction = 0.35
    var scroll_position = twitter_block.scrollTop

    function twitter_block_scroll() {
        scroll_position += scroll_direction
        twitter_block.scrollTop = scroll_position
        if (scroll_position < 0 || scroll_position > twitter_block_height) {
            scroll_direction *= -1
        }
        requestAnimationFrame(twitter_block_scroll)
    }

    twitter_block_scroll()
});