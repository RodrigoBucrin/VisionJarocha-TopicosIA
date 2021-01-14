extends RigidBody2D

const UP_IMPULSE: float = -155.0
var puntos = 0

func _input(event: InputEvent) -> void:
	if event is InputEventKey:
		if event.is_action_pressed("ui_select"):
			_Kruger_jump()
			
func _Kruger_jump() -> void:
	set_linear_velocity(Vector2(0, 0))
	apply_central_impulse(Vector2(0, UP_IMPULSE))
	#$FlapAnimationPlayer.stop()
	#$FlapAnimationPlayer.play("Flap")




func _on_PUNTO_body_exited(body):
	pass


func _on_PUNTO_body_entered(body):
	puntos= puntos + 1
	$"../PUNTAJE".set_text(str(puntos))
	print(puntos)
