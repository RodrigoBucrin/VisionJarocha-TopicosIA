extends Node2D

const SMOOTH_SPEED = -.5
var position_difference = Vector2()
var smoothed_velocity = Vector2()

func _process(delta):
	var destination = $"Sprite/CACTUS".global_position

	position_difference = destination - position
	smoothed_velocity = position_difference * SMOOTH_SPEED * delta

	position += smoothed_velocity




func _on_Area2D_body_entered(body):
	print(body)
	get_tree().reload_current_scene()
